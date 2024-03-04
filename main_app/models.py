from django.db import models

class Tot(models.Model):
  name = models.CharField(max_length=100)
  gender = models.CharField(max_length=100)
  age = models.IntegerField()
  description = models.TextField(max_length=300)

def __str__(self):
    return self.name 