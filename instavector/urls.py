from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import PostListView


urlpatterns=[
    url('^$',PostListView.as_view(),name = 'index'),
    url('accounts/', include('django.contrib.auth.urls')),
    
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)