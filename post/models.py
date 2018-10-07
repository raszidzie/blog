from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    published = models.DateField()


    def __str__(self):
        return self.title