from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .models import Image,Comment,Profile
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    form = UserCreationForm()
    return render(request, 'registration/registration_form.html',{'form':form})

@login_required(login_url='/accounts/login/')
def index(request):
    images = Image.get_images()
    return render(request,'index.html',{"images":images})



