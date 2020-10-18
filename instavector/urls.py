from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import PostListView
from django.contrib.auth.decorators import login_required



urlpatterns=[
    url('^$',login_required( PostListView.as_view()),name = 'index'),
    
    #url(r'^post/(\d+)/update/',views.update_post,name = 'update'),
    url(r'^post/(\d+)',views.detail,name = 'detail'),
    url('accounts/', include('django.contrib.auth.urls'))
   
    
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)