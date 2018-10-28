from django.shortcuts import render, get_object_or_404,redirect
from .models import Post,Comment,Contact,Subscribe
from .forms import PostForm, CommentForm, ContactForm, EmailForm
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def home(request):
    
   

    return render (request, 'index.html')

def blog(request):
    posts = Post.objects.all()
    return render (request, 'blog.html', {"posts":posts})    


def post_index(request):
    form = EmailForm(request.POST or None)
    if form.is_valid():
        mail = form.save()
        return redirect ('home')
   
  
    posts = Post.objects.all().order_by('-id')[:3]
    return render (request, 'index.html', {"posts":posts, 'form':form})    

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    posts = Post.objects.all().order_by('-id')[:3]
    postss= Post.objects.all().order_by('-published')[1:4]
    form = CommentForm(request.POST or None)
   
    
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return redirect (post.get_absolute_url())

    comments= Comment.objects.all().count()   


    context = {
        'post':post,
        'form':form,
        'posts':posts,
        'comments':comments,  
        'postss':postss,    
        }
    return render (request, 'post/detail.html', context )


@login_required
def adminpost(request):
   
    contacts = Contact.objects.all()
    mails = Subscribe.objects.all()
    context = {
       
        'contacts':contacts,
        'mails':mails,
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

def listing(request): 
   posts = Post.objects.all()
   
   paginator = Paginator(posts, 4)
   page = request.GET.get('page')
   if not page:
    page = paginator.num_pages

   postss= Post.objects.all().order_by('-published')[4:8]
   
   
   
   try:
        posts = paginator.page(page)
   except PageNotAnInteger:
        posts = paginator.page(1)
   except EmptyPage:
        posts = paginator.page(paginator.num_pages)
   

   return render(request, 'blog.html', { 'posts':posts , 'postss':postss})