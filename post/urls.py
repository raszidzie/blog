from django.conf.urls import include, url
from .views import post_index,post_detail,adminpost,post_create
from django.conf import settings 
from django.conf.urls.static import static 
app_name = "blog"
urlpatterns = [
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^index/', post_index, name="index"),
    url(r'^(?P<id>\d+)/$', post_detail, name="detail" ),
    url(r'^dashboard/', adminpost, name="dashboard"),
    url(r'^create/', post_create, name="create"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
