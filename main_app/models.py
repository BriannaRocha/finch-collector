from django.db import models
from django.urls import reverse

class Tot(models.Model):
  name = models.CharField(max_length=100)
  gender = models.CharField(max_length=100)
  age = models.IntegerField()
  description = models.TextField(max_length=300)

def __str__(self):
    return self.name 

def get_absolute_url(self):
    return reverse('tot-detail', kwargs={'tot_id': self.id})