from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import PostListView, PostDetailView



urlpatterns=[
    url('^$',PostListView.as_view(),name = 'index'),
    url(r'^post/(\d+)',views.detail,name = 'detail'),
    url('accounts/', include('django.contrib.auth.urls')),
   
    
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)