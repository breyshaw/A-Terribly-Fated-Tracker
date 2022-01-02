from django.shortcuts import render
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