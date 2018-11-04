from django.conf.urls import include, url
from .views import *
from django.conf import settings 
from django.conf.urls.static import static 
app_name = "elan"
urlpatterns = [
   
    
    url(r'^main/',elan, name="main" ),
    url(r'^(?P<id>\d+)/$', elandetail, name="elandetail" ),
    url(r'^elanlar/', store, name="store" ),
    url(r'^kids/', kids, name="kids" ),
    url(r'^work/', work, name="work" ),
    url(r'^service/', service, name="service" ),
    url(r'^personal/', personal, name="personal" ),
    url(r'^apartment/', apart, name="apart" ),
    url(r'^education/', education, name="edu" ),
    url(r'^elanadmin/', elanadmin, name="elanadmin" ),
    url(r'^(?P<id>\d+)/update/$', elan_update, name="elanupdate" ),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)