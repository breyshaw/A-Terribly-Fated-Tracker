from django.db import models
from django.contrib.auth.models import User

class Mask(models.Model):
  name = models.CharField(max_length=100)
  details = models.TextField(max_length=250)
  guide = models.CharField(max_length=500)
  img_url = models.CharField(max_length=100, blank=True)

  def __str__(self):
    return self.name

class File(models.Model):
  name = models.CharField(max_length=100)
  date = models.DateField('Start Date')
  mask_inventory = models.ManyToManyField(Mask)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name