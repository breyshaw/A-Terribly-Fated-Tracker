from django.db import models
from django.contrib.auth.models import User

class Mask(models.Model):
  name = models.CharField(max_length=100)
  details = models.TextField(max_length=500)
  guide = models.TextField(max_length=500)
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

class Photo(models.Model):
  url = models.CharField(max_length=250)
  mask = models.OneToOneField(Mask, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for mask_id: {self.mask_id} @{self.url}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    isAdmin = models.BooleanField(default=False)