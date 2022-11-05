from unittest.util import _MAX_LENGTH
from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime


# Create your models here.
class Credit(models.Model):
    code = models.IntegerField()
    description = models.CharField(max_length=40)
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   
    
    def __str__(self):
        return f"{self.code} {self.description} | amount: {self.amount}"