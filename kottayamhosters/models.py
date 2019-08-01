from django.db import models

# Create your models here.
class Add_logo(models.Model):
    name = models.CharField(max_length=250)
    description_logo = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='uploaded_pictures/photo', blank=True, null=True)
class Add_video(models.Model):
    video_name = models.CharField(max_length=250)
    video_description_logo = models.TextField(blank=True, null=True)
    video_photo = models.ImageField(upload_to='uploaded_pictures/photo', blank=True, null=True)
class Add_design(models.Model):
    design_name = models.CharField(max_length=250)
    design_description_logo = models.TextField(blank=True, null=True)
    design_photo = models.ImageField(upload_to='uploaded_pictures/photo', blank=True, null=True)
class Add_printart(models.Model):
    printart_name = models.CharField(max_length=250)
    printart_description_logo = models.TextField(blank=True, null=True)
    printart_photo = models.ImageField(upload_to='uploaded_pictures/photo', blank=True, null=True)