from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Image(models.Model):
    author  = models.ForeignKey(User, on_delete=models.CASCADE, null='True', blank=True)
    image = models.ImageField(upload_to = 'pics/')
    name = models.CharField(max_length=50,blank=True)	   
    caption = models.CharField(max_length=250, blank=True)	
    likes =  models.ManyToManyField(User, related_name='likes', blank=True, )
    date_posted = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk':self.pk})

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def total_likes(self):
        return self.likes.count()

    @classmethod
    def get_images(cls):
        images = cls.objects.all()
        return images

    @property
    def get_all_comments(self):
        return self.comments.all()

    class Meta:
        ordering = ["-date_posted"]

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='images/', default='default.png')
    bio = models.TextField(max_length=500, default="My Bio", blank=True)	  

    def __str__(self):
        return f'{self.user.username} Profile'

class Comment(models.Model):
    comment = models.TextField()
    image = models.ForeignKey('Image', on_delete=models.CASCADE,related_name='comments',null='True', blank=True )
    name = models.CharField(max_length=100, blank=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comments',null='True', blank=True )
    created = models.DateTimeField(auto_now_add=True, null=True)  

    def __str__(self):
        return f'{self.image.name} comment'

    class Meta:
        ordering = ["-pk"]