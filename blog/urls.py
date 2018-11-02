from django.conf.urls import include, url
from django.contrib import admin
from post.views import home,post_index,blog,listing
from django.conf import settings 


from django.conf.urls.static import static 


urlpatterns = [
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', post_index, name="home"),
    url(r'^/blog', listing, name="blogpage"),
    url(r'post/', include('post.urls', namespace="blog")),
    url(r'accounts/', include('accounts.urls', namespace="accounts")),
    url(r'elan/', include('elan.urls', namespace="elanlar")),
  
    
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
