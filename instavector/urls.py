from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
#from .views import PostListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views



urlpatterns=[
    url('^$',views.index,name = 'index'),
    url('accounts/', include('django.contrib.auth.urls')),
   
    url('register/', views.register, name='register'),
    #url('login/', auth_views.LoginView.as_view(), name='login'),
    url('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    url('profile/', views.profile, name='profile'),
    url('user/<username>/', views.user_profile, name='user'),
    url(r'post/(\d+)/delete',views.delete_post,name = 'delete'),
    url(r'post/new/',views.create_post,name = 'create'),
    #url(r'post/(\d+)/comment',views.comment,name = 'comment'),
    url(r'like/(\d+)',views.like_post,name = 'like'),
    url(r'follow/(\d+)',views.follow,name = 'follow'),
    url(r'post/(\d+)',views.detail,name = 'detail'),
    url(r'^search/', views.search_results, name='search'),
   
    
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)