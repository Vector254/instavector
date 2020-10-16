from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to = 'pics/')
    name = models.CharField(max_length=50,blank=True)	   
    caption = models.CharField(max_length=250, blank=True)	
    likes =  models.ManyToManyField(User, related_name='likes', blank=True, )
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, null='True', blank=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(upload_to='images/', default='default.png')
    bio = models.TextField(max_length=500, default="My Bio", blank=True)	  

class Comment(models.Model):
    comment = models.TextField()
    image = models.ForeignKey('Image', on_delete=models.CASCADE,null='True', blank=True )
    user = models.ForeignKey('Profile', on_delete=models.CASCADE,null='True', blank=True )
    created = models.DateTimeField(auto_now_add=True, null=True)  