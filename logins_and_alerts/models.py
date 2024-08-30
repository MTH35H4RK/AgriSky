from django.db import models
from django.utils import timezone
import os
from django.contrib.auth.models import AbstractBaseUser, UserManager

def custom_upload_to(instance, filename):
    extension = filename.split('.')[-1]
    filename = '{0}.{1}'.format(instance.username, extension)
    full_path = os.path.join('newstuff/static/images/avatar/', filename)
    if os.path.exists(full_path):
        os.remove(full_path)  
    return 'newstuff/static/images/avatar/{0}'.format(filename)

class CUser(models.Model):
    username = models.CharField(max_length=15,unique=True)
    password = models.CharField(max_length=15)
    displayname = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField('User Email')
    title = models.CharField(max_length=20)
    description = models.TextField(blank=True)

    avatar = models.ImageField(null=True,blank=True,upload_to=custom_upload_to)

    USERBG_CHOICES = [
        ('default', 'Default'),
        ('stars', 'Stars'),
    ]
    userbg = models.CharField(blank=True,
                              max_length=30,
                              choices=USERBG_CHOICES,
                              default="default")

    is_in_team = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_dark_theme = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Drone(models.Model):
    dronename = models.CharField('Drone',max_length=7)
    location = models.CharField(max_length=30)
    battiere = models.CharField('Battiere Percent',max_length=3)
    url = models.URLField(blank=True)
    active = models.BooleanField('Status')

    def __str__(self):
        return self.dronename

class Alert(models.Model):
    alertname = models.CharField('Alert',max_length=30)
    dronetarget = models.ForeignKey(Drone,on_delete=models.PROTECT)
    alertdescription = models.TextField('Description')
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.alertname
