from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate

# Create your views here.


# Create your views here.
@login_required(login_url='login')
def index(request):
    return render(request,'index.html')

