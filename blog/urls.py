from django.conf.urls import include, url
from django.contrib import admin
from post.views import home,contact
from django.conf import settings 
from django.conf.urls.static import static 


urlpatterns = [
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', contact, name="home"),
    url(r'post/', include('post.urls', namespace="blog")),
    url(r'accounts/', include('accounts.urls', namespace="accounts")),

    
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
