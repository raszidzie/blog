from django.shortcuts import render, get_object_or_404,redirect
from .models import Post,Comment,Contact
from .forms import PostForm, CommentForm, ContactForm
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
  

    return render (request, 'home.html' )

def post_index(request):
    posts = Post.objects.all()
    return render (request, 'index.html', {"posts":posts})    

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    form = CommentForm(request.POST or None)
   
    
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return redirect (post.get_absolute_url())
    context = {
        'post':post,
        'form':form,
      }
    return render (request, 'post/detail.html', context )
@login_required
def adminpost(request):
   
    contacts = Contact.objects.all()

   
    
   
    context = {
       
        'contacts':contacts,
      }
    return render (request, 'admin.html', context)
@login_required
def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    
    posts = Post.objects.all()
   
    if form.is_valid():
        post = form.save()
        
        
    context={
        'form':form,
        'posts':posts,
    }
    return render (request, 'post/meqale.html',context)
@login_required
def post_update(request, id):
    post = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        post = form.save()
        return redirect ('blog:create')
      
    context = {
        'post':post,
      }
    return render (request, 'post/update_post.html', context )
@login_required
def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect ('blog:create')

def contact (request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
    context={
        'form':form,
    }    
    return render (request, 'home.html',context)
