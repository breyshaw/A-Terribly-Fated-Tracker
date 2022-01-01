from django.shortcuts import render
from django.http import HttpResponse

def home(request):
  return HttpResponse('Home view works!')

# For testing with the templates, may keep this page...
def about(request):
  return render(request, 'about.html')


# Simulating Masks for testing purposes
class Mask:
  def __init__(self, name, details, guide):
    self.name = name
    self.details = details
    self.guide = guide

masks = [
  Mask('Deku Mask', 'Change into the body of a deceased Deku','Finish the first three days..'),
  Mask('Zora Mask', 'Change into the body of a deceased Zora','Play the song of healing for the zora at the great bay'),
  Mask('Goron Mask', 'Change into the body of a deceased Goron','Play the song of healing for the Goron in Snowhead')
]

def masks_index(request):
  return render(request, 'masks/index.html', { 'masks': masks })