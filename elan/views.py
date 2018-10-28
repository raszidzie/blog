from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Elan

def elan(request):
     items =  Elan.objects.all().order_by('-id')[:6]
     itemsmost = Elan.objects.all().order_by('-id')[3:4]
     context ={
         'items':items
     }
     return render (request, 'elan/elanlar.html', context )

def elandetail(request, id):
    item = get_object_or_404(Elan, id=id)
    
    
    return render (request, 'elan/elandetail.html')