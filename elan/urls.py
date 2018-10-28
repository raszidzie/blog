from django.conf.urls import include, url
from .views import elan, elandetail
from django.conf import settings 
from django.conf.urls.static import static 
app_name = "elan"
urlpatterns = [
   
    
    url(r'^esas/',elan ),
     
    url(r'^(?P<id>\d+)/$', elandetail, name="elandetail" ),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)