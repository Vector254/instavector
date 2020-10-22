from django.shortcuts import render,redirect, get_object_or_404
from django.http  import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .models import Image,Comment,Profile
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserRegistrationForm, PostForm, CommentForm, UserUpdateForm, ProfileUpdateForm
from django.views.generic import DetailView
from django.db.models.base import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse
from django.db.models import Q
from itertools import chain

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
            current_user = Profile.objects.get(name=request.user)
            add.author = current_user
            add.save()
            return redirect('index')
    

    context = {'form':form}
    return render(request,'image_form.html',context)

@login_required
def index(request):
    images=Image.objects.all()
    #get logged in user profile
    profile = Profile.objects.get(name=request.user)
    # check who we are following
    users = [user for user in profile.following.all()]
    #variables
    posts=[]
    qs= None
    #get posts of people we are following
    for u in users:
        p = Profile.objects.get(name=u)
        p_posts = p.profile_posts()
        posts.append(p_posts)
    #get our posts
    my_posts=profile.profile_posts()
    posts.append(my_posts)
    #unpack posts list
    qs = sorted(chain(*posts), reverse=True, key=lambda obj: obj.date_posted)

    context = {'profile':profile,'posts':qs}
       
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
    #user_profile = get_object_or_404(User, pk=pk)
   
    if request.method=='POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
           user_form.save() 
           profile_form.save()
           messages.success(request, f'Profile info updated successfully!')
           return redirect('profile' )

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

def follow_unfollow(request):
    if request.method == 'POST':
        my_profile = Profile.objects.get(name=request.user)
        pk = request.POST.get('profile_pk')
        obj = Profile.objects.get(pk=pk)

        if obj.name in my_profile.following.all():
            my_profile.following.remove(obj.name)
        else:
            my_profile.following.add(obj.name)
        return redirect(request.META.get('HTTP_REFERER')) 
    return redirect('explore')


def search_results(request):

    if 'query' in request.GET and request.GET["query"]:
        search_term = request.GET.get("query")
        searched_images = Image.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched!"
        return render(request, 'search.html',{"message":message})


def explore(request):

    users=Profile.objects.exclude(name=request.user)
   
    
    return render(request,'explore.html', {'users':users,})

class ProfileDetailView(DetailView):
    model = Profile
    template = "profile_detail.html"
    #get user profile
    def get_object(self, **kwargs):
        pk = self.kwargs.get('pk')
        view_profile = Profile.objects.get(pk=pk)
        return view_profile

    #get my profile
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        view_profile = self.get_object()
        my_profile = Profile.objects.get(name=self.request.user)
        if view_profile.name in my_profile.following.all():
            follow = True
        else:
            follow =False
        context["follow"] = follow
        return context
    

