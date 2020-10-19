from django.shortcuts import render,redirect, get_object_or_404
from django.http  import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .models import Image,Comment,Profile
from django.contrib import messages
from .forms import UserRegistrationForm, PostForm, CommentForm, UserUpdateForm, ProfileUpdateForm
from django.views.generic import ListView, DeleteView
from django.db.models.base import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse
from django.db.models import Q

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
    liked = False
    
  
    context = {'images':images,}
       
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
    total_likes = pic.total_likes()
    liked = False
    if pic.likes.filter(id=request.user.id).exists():
        liked=True

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
        'form': form,
        'total_likes':total_likes,
        'liked':liked}

    return render(request,"post_detail.html", params)
    
    
    

@login_required
def profile(request):
    images = Image.objects.all()
    if request.method=='POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
           user_form.save() 
           profile_form.save()
           messages.success(request, f'Profile info updated successfully!')
           return redirect('profile')

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    params = {
        'images':images,
        'user_form':user_form,
        'profile_form':profile_form,
    }
   
    return render(request, 'profile.html', params)


@login_required
def user_profile(request, username):
    users = get_object_or_404(User, username=username)
    if request.user == users:
        return redirect('profile', username=request.user.username)
    posts = users.profile.images.all()
    params = {
        'users': users,
        'posts': posts,
    }

    return render(request, 'user_profile.html', params)

@login_required
def like_post(request, pk):
    post = get_object_or_404(Image, id=pk)
    liked= False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked=False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('detail', args=[str(pk)]))

def follow(request, pk):
    profile = get_object_or_404(Profile, id=pk)
    followed= False
    if profile.follows.filter(id=request.user.id).exists():
        profile.follows.remove(request.user)
        followed= False
    else:
        profile.follows.add(request.user)
        followed = True
        return HttpResponseRedirect(reverse('profile', args=[str(pk)]))


def search_results(request):

    if 'query' in request.GET and request.GET["query"]:
        search_term = request.GET.get("query")
        searched_images = Image.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched!"
        return render(request, 'search.html',{"message":message})




