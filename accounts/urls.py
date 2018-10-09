from django.conf.urls import include, url
from django.contrib import admin
from .views import login_view



urlpatterns = [
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^login/', login_view),
    
]  
