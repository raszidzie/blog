from django.shortcuts import render, get_object_or_404,redirect,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Elan, ElanComment
from .forms import CommentForm,ElanForm

def elan(request):
     items =  Elan.objects.all().order_by('-id')[:3]
     itemsmost = Elan.objects.all().order_by('-id')[3:4]
     kidsCategory = Elan.objects.all().filter(itemCategory="kids")[:6]
     eduCategory = Elan.objects.all().filter(itemCategory="education")[:6]
     workCategory = Elan.objects.all().filter(itemCategory="work")[:6]
     serviceCategory = Elan.objects.all().filter(itemCategory="service")[:6]
     personalCategory = Elan.objects.all().filter(itemCategory="service")[:6]
     apartCategory = Elan.objects.all().filter(itemCategory="service")[:6]
    

     context ={
         'items':items,
         'kidsCategory':kidsCategory,
         'eduCategory':eduCategory,
         'workCategory':workCategory,
         'serviceCategory': serviceCategory,
         
     }
     return render (request, 'elan/elanlar.html', context )

def elandetail(request, id):
    
    elan = get_object_or_404(Elan, id=id)
    form = CommentForm(request.POST or None)
   
    
    if form.is_valid():
        comment = form.save(commit=False)
        comment.elan = elan
        comment.save()
        
     
    items =  Elan.objects.all()[:4]
    comments= ElanComment.objects.all()  
    


    context ={
        'elan':elan,
        'form':form,
        'comments':comments,
        'items':items,
    }
    
    
    return render (request, 'elan/elandetail.html', context)

def store(request):
    itemsnew =  Elan.objects.all().order_by('-id')[:3]
    items =  Elan.objects.all()
   
    context={
        'items':items,
        'itemsnew':itemsnew,
    }
    return render (request, 'elan/elans.html', context)

def kids (request):
   itemsnew =  Elan.objects.all().order_by('-id')[:3]
   items = Elan.objects.all().filter(itemCategory="kids")
   paginator = Paginator(items, 6)
   page = request.GET.get('page')

   try:
        items = paginator.page(page)
   except PageNotAnInteger:
        items = paginator.page(1)
   except EmptyPage:
        items = paginator.page(paginator.num_pages)
   
   
   context={
         'items':items,
        'itemsnew':itemsnew,
    }
   return render (request, 'elan/elans.html', context)

def work (request):
    itemsnew =  Elan.objects.all().order_by('-id')[:3]
    items =  Elan.objects.all().filter(itemCategory="work")
    paginator = Paginator(items, 6)
    page = request.GET.get('page')

    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
   
    context={
        'items':items,
        'itemsnew':itemsnew,
    }
    return render (request, 'elan/elans.html', context)

def education (request):
    itemsnew =  Elan.objects.all().order_by('-id')[:3]
    items =  Elan.objects.all().filter(itemCategory="education")
    paginator = Paginator(items, 6)
    page = request.GET.get('page')
 
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages) 
   
    context={
        'items':items,
        'itemsnew':itemsnew,
    }
    return render (request, 'elan/elans.html', context)

def service (request):
    itemsnew =  Elan.objects.all().order_by('-id')[:3]
    items =  Elan.objects.all().filter(itemCategory="service")
    paginator = Paginator(items, 6)
    page = request.GET.get('page')
 
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
   
    context={
        'items':items,
        'itemsnew':itemsnew,
    }
    return render (request, 'elan/elans.html', context)

def personal (request):
    itemsnew =  Elan.objects.all().order_by('-id')[:3]
    items =  Elan.objects.all().filter(itemCategory="personal")
    paginator = Paginator(items, 6)
    page = request.GET.get('page')

    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
   
    context={
        'items':items,
        'itemsnew':itemsnew,
    }
    return render (request, 'elan/elans.html', context)    

def apart (request):
    itemsnew =  Elan.objects.all().order_by('-id')[:3]
    items =  Elan.objects.all().filter(itemCategory="apart")
    paginator = Paginator(items, 6)
    page = request.GET.get('page')

    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
   
    context={
        'items':items,
        'itemsnew':itemsnew,
    }
    return render (request, 'elan/elans.html', context)    


@login_required
def elanadmin(request):
   
    form = ElanForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form = form.save(commit=False)
        form.user = request.user
        form.save()
    items = Elan.objects.all()
   
    context = {
       
        'form':form,
        'items':items,
        
      }
    return render (request, 'elan/elancreate.html', context)    

@login_required
def elan_update(request, id):
    elan = get_object_or_404(Elan, id=id)
    form = ElanForm(request.POST or None, request.FILES or None, instance=elan)
    if form.is_valid():
        elan=form.save()
        return redirect('elanlar:elanadmin')
    context={
        'elan':elan
    }   
    return render (request, 'elan/elanupdate.html', context) 