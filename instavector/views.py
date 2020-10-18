from django.shortcuts import render,redirect, get_object_or_404, HttpResponseRedirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .models import Image,Comment,Profile
from django.contrib import messages
from .forms import UserRegistrationForm, PostForm, CommentForm
from django.views.generic import ListView, DeleteView
from django.db.models.base import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created successfully!')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/registration_form.html',{'form':form})




@login_required
def create_post(request):
    current_user = request.user
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES or None)
        if form.is_valid():
            add=form.save(commit=False)
            add.author = current_user
            add.save()
            return redirect('index')
    

    context = {'form':form}
    return render(request,'image_form.html',context)

@login_required
def index(request):
    images = Image.objects.all()
    
  
    context = {'images':images}
       
    return render(request, 'index.html', context)


@login_required
def delete_post(request, post_id): 
    # dictionary for initial data with  
    # field names as keys 
    context ={} 
    post = Image.objects.get(pk=post_id)
    if request.method =="POST": 
            #check if owner before delete permision
        if post.author == request.user:
                # delete object 
            post.delete() 
        else:

            messages.error(request, f'Permission denied!')    
            # after deleting redirect to  
            # home page 
        return redirect("index") 

    return render(request, "post_confirm_delete.html", context) 



def detail(request,post_id):
   
    image = Image.objects.get(id=post_id)
    pic = get_object_or_404(Image, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            savecomment = form.save(commit=False)
            savecomment.image = pic
            savecomment.user = request.user.profile
            savecomment.save()
            return redirect('index')
    else:
        form = CommentForm()
    params = {
        'image': image,
        'pic':pic,
        'form': form,}

    return render(request,"post_detail.html", params)
    
    
    

@login_required
def profile(request):
    posts = Image.get_images()
    return render(request,'profile.html',{"posts":posts})


@login_required
def like_post(request):
    post = get_object_or_404(Image, id=request.POST.get('post_id') )
    post.likes.add(request.user)
    return redirect('index')




