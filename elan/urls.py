from django.conf.urls import include, url
from .views import elan
from django.conf import settings 
from django.conf.urls.static import static 
app_name = "elan"
urlpatterns = [
   
    
     url(r'^esas/',elan ),


] 