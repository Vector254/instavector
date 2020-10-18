from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .models import Image,Comment,Profile
from django.contrib import messages
from .forms import UserRegistrationForm, PostForm
from django.views.generic import ListView, CreateView, UpdateView
from django.db.models.base import ObjectDoesNotExist

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for successfully!')
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




class PostListView(ListView):
    model = Image 
    template_name = 'index.html'
    context_object_name = 'images' 
    ordering = ['-date_posted']



def detail(request,post_id):
    try:
        image = Image.objects.get(id=post_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,"post_detail.html", {"image":image})
    
    
    

@login_required
def profile(request):
    posts = Image.get_images()
    return render(request,'profile.html',{"posts":posts})






