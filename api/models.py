from enum import auto
from turtle import update
from django.db import models

# Create your models here.

class Note(models.Model):
  body = models.TextField(null=True, blank=True)
  
  #date off the update
  update = models.DateField(auto_now=True)
  
  # date off the creation
  created = models.DateTimeField(auto_now_add=True)
  
  def __str__(self) -> str:
      return self.body[0:50]
    

  
