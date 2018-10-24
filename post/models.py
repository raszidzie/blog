from django.db import models

from django.core.urlresolvers import reverse
# Create your models here.
class Post(models.Model):
    user = models.ForeignKey('auth.user', verbose_name="Yazar",default=1)
    title = models.CharField(max_length=120)
    category = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    source = models.CharField(max_length=300, blank=True)
    person = models.CharField(max_length=50, blank=True)
    published = models.DateField( auto_now_add=True)
    image = models.FileField(null=True, blank=True)
    tag = models.CharField(max_length="200", blank=True)
  


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'id': self.id})    

class Comment(models.Model):
    post = models.ForeignKey('post.Post', related_name='comments', on_delete=models.CASCADE)


    name= models.CharField(max_length=200, verbose_name="Ad")
    comment = models.TextField(verbose_name="Yorum")
    date = models.DateTimeField(auto_now_add=True)

class Contact(models.Model):
    ad = models.CharField(max_length=200)
    soyad = models.CharField(max_length=200)
    sual = models.CharField(max_length=600)