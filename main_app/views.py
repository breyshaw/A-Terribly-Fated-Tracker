from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Mask, File

def home(request):
  return render(request, 'home.html')

# For testing with the templates, may keep this page...
def about(request):
  return render(request, 'about.html')

def masks_index(request):
  masks = Mask.objects.all()
  return render(request, 'masks/index.html', { 'masks': masks })

def masks_detail(request, mask_id):
  mask = Mask.objects.get(id=mask_id)
  return render(request, 'masks/detail.html', { 'mask': mask })

def files_index(request):
  files = File.objects.all()
  return render(request, 'files/index.html', { 'files': files })

def files_detail(request, file_id):
  file = File.objects.get(id=file_id)
  masks_file_doesnt_have = Mask.objects.exclude(id__in = file.mask_inventory.all().values_list('id'))
  return render(request, 'files/detail.html', { 'file': file, 'masks' : masks_file_doesnt_have })

# By convention, the FileCreate CBV will look to render a template named templates/main_app/file_form.html
class FileCreate(CreateView):
  model = File
  fields = '__all__'
  success_url = '/files/'

class FileUpdate(UpdateView):
  model = File
  fields = '__all__'

class FileDelete(DeleteView):
  model = File
  success_url = '/files/'