from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .models import Image,Comment,Profile

# Create your views here.


# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    images = Image.get_images()
    return render(request,'index.html',{"images":images})

