from unittest.util import _MAX_LENGTH
from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime

# Create your models here.
class Customer(models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=40)
    email = models.EmailField()
    segment = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   
    
    def __str__(self):
        return f"{self.code} {self.name} | email: {self.email} | segment: {self.segment}"