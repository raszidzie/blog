from django.contrib import admin
from .models import Elan
# Register your models here.
class ElanAdmin(admin.ModelAdmin):
    
    class Meta:

        model = Elan
admin.site.register(Elan,ElanAdmin)        