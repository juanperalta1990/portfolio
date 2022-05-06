from django.db import models
from django.db.models.fields import CharField, URLField, TextField
from django.db.models.fields.files import ImageField

# Create your models here.

class Project(models.Model):
    title= CharField(max_length=100)
    description= TextField(max_length=500)
    image= ImageField(upload_to='portfolio-images/', blank=True)
    url= URLField(blank=True)

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title


class Curriculum(models.Model):
   title = models.CharField(max_length=50)
   file = models.FileField(upload_to="files/", null=True, blank=True)
   
   def __str__(self):
        return self.title