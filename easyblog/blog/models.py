from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    date = models.DateField(auto_now_add=True)
    text = models.TextField()
    image = models.ImageField()
    
