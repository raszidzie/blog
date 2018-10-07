from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm
# Create your views here.
def home(request):
  

    return render (request, 'home.html' )

def post_index(request):
    posts = Post.objects.all()
    return render (request, 'index.html', {"posts":posts})    

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    context = {
        'post':post,
      }
    return render (request, 'post/detail.html', context )

def adminpost(request):
   
    return render (request, 'admin.html')

def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save()
      
    context={
        'form':form,
    }
    return render (request, 'post/meqale.html',context)
