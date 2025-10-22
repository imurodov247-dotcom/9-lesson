from django.db import models

# Create your models here.
class Profile(models.Model):
    nomi = models.CharField(max_length=40) 
    image = models.ImageField(upload_to='images/')   