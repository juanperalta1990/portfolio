from django.db import models
from django.db.models.fields import CharField, URLField, TextField
from django.db.models.fields.files import ImageField

# Create your models here.

class Project(models.Model):
    title= CharField(max_length=100)
    description= TextField(max_length=500)
    image= ImageField(upload_to='portfolio/images')
    url= URLField(blank=True)