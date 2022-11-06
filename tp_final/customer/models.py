from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models
from ckeditor.fields import RichTextField

from datetime import datetime
from unittest.util import _MAX_LENGTH

# Create your models here.
class Customer(models.Model):
    code = models.IntegerField(null=False, blank=False)
    name = models.CharField(max_length=40, null=False, blank=False)
    email = models.EmailField()
    segment = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='customer', null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    comments = models.ManyToManyField(
        User, through="Comment", related_name="comments_owned"
    )      
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   
    class Meta:
        unique_together = (
            "code",
            "name",
        )
        ordering = ["-created_at"]    
        
    def __str__(self):
        return f"{self.code} {self.name} | email: {self.email} | segment: {self.segment}"
    
class Comment(models.Model):
    text = models.TextField(
        validators=[
            MinLengthValidator(10, "El comentario debe ser mayor de 10 caracteres")
        ]
    )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    