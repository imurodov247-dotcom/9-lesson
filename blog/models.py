from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = HTMLField()
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to="images")
    author = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
    