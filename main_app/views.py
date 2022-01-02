from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from .models import Mask, File, Photo
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import boto3

S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'a-terrible-tracker'

class Home(LoginView):
  template_name = 'home.html'

# For testing with the templates, may keep this page...
def about(request):
  return render(request, 'about.html')

def masks_index(request):
  masks = Mask.objects.all()
  return render(request, 'masks/index.html', { 'masks': masks })

def masks_detail(request, mask_id):
  mask = Mask.objects.get(id=mask_id)
  return render(request, 'masks/detail.html', { 'mask': mask })

@login_required(login_url='/')
def files_index(request):
  files = File.objects.filter(user=request.user)
  return render(request, 'files/index.html', { 'files': files })

@login_required(login_url='/')
def files_detail(request, file_id):
  file = File.objects.get(id=file_id)
  masks_file_doesnt_have = Mask.objects.exclude(id__in = file.mask_inventory.all().values_list('id'))
  return render(request, 'files/detail.html', { 'file': file, 'masks' : masks_file_doesnt_have })

@login_required(login_url='/')
def assoc_mask(request, file_id, mask_id):
  File.objects.get(id=file_id).mask_inventory.add(mask_id)
  return redirect('files_detail', file_id=file_id)

@login_required(login_url='/')
def remove_mask(request, file_id, mask_id):
  File.objects.get(id=file_id).mask_inventory.remove(mask_id)
  return redirect('files_detail', file_id=file_id)

@login_required(login_url='/')
def add_photo(request, mask_id):
  # photo-file will be the "name" attribute on the <input type="file">
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    # need a unique "key" for S3 / needs image file extension too
		# uuid.uuid4().hex generates a random hexadecimal Universally Unique Identifier
    # Add on the file extension using photo_file.name[photo_file.name.rfind('.'):]
    key = uuid.uuid4().hex + photo_file.name[photo_file.name.rfind('.'):]
    # just in case something goes wrong
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      # build the full url string
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      photo = Photo(url=url, mask_id=mask_id)
      # Remove old photo if it exists
      mask_photo = Photo.objects.filter(mask_id=mask_id)
      if mask_photo.first():
        mask_photo.first().delete()
      photo.save()
    except Exception as err:
      print('An error occurred uploading file to S3: %s' % err)
  return redirect('masks_detail', mask_id=mask_id)

# By convention, the FileCreate CBV will look to render a template named templates/main_app/file_form.html
class FileCreate(LoginRequiredMixin, CreateView):
  model = File
  fields = ['name', 'date', 'mask_inventory']
  success_url = '/files/'
  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the save file
    return super().form_valid(form)

class FileUpdate(LoginRequiredMixin, UpdateView):
  model = File
  fields = ['name', 'date', 'mask_inventory']

class FileDelete(LoginRequiredMixin, DeleteView):
  model = File
  success_url = '/files/'


def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in
      login(request, user)
      return redirect('files_index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)