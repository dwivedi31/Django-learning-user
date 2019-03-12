from django.db import models
from django.contrib.auth.models import User
from django.contrib import auth
# Create your models here.

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #additional
    protofolio_site = models.URLField(blank = True)

    profile_pic = models.ImageField(upload_to ='profile_pics',blank=True)

    def __str__(self):
        return self.user.username
