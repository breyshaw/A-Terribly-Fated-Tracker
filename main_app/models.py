from django.db import models

class Mask(models.Model):
  name = models.CharField(max_length=100)
  details = models.TextField(max_length=250)
  guide = models.CharField(max_length=500)

  def __str__(self):
    return self.name
