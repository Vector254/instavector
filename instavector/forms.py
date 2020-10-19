from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Image, Comment


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

# creating a form 
class PostForm(forms.ModelForm): 
  
    # create meta class 
    class Meta: 
        # specify model to be used 
        model = Image 
  
        # specify fields to be used 
        fields = [ 
            "image", 
            "name",
            "caption", 
        ] 

class CommentForm(forms.ModelForm): 
  
    # create meta class 
    class Meta: 
        # specify model to be used 
        model = Comment 
  
        # specify fields to be used 
        fields = [ 
            "comment", 
            
        ] 