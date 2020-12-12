from django.db import models

# Create your models here.
class Event(models.Model):

    # Header
    logo = models.ImageField(default='logo',upload_to = 'event_images/')

    # Intro
    image = models.ImageField(upload_to = 'event_images/',default='bg')
    text = models.CharField(max_length=300)

    # Second
    stitle = models.CharField(max_length=300,default='No Title')
    stext = models.TextField(default='No text')

