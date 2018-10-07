from django.conf.urls import include, url
from django.contrib import admin
from post.views import home


urlpatterns = [
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home),
    url(r'post/', include('post.urls', namespace="blog"), ),
]
