from django.shortcuts import render
from .models import Mask

def home(request):
  return render(request, 'home.html')

# For testing with the templates, may keep this page...
def about(request):
  return render(request, 'about.html')

def masks_index(request):
  masks = Mask.objects.all()
  return render(request, 'masks/index.html', { 'masks': masks })