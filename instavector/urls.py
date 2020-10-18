from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
#from .views import PostListView
from django.contrib.auth.decorators import login_required



urlpatterns=[
    url('^$',views.index,name = 'index'),
    url(r'post/(\d+)/delete',views.delete_post,name = 'delete'),
    url(r'post/new/',views.create_post,name = 'create'),
    #url(r'post/(\d+)/comment',views.comment,name = 'comment'),
    url(r'like/(\d+)',views.like_post,name = 'like'),
    url(r'post/(\d+)',views.detail,name = 'detail'),
    url('accounts/', include('django.contrib.auth.urls'))
   
    
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)