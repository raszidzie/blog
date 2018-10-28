from django import forms
from .models import Post, Comment, Contact, Subscribe

class PostForm(forms.ModelForm):

    class Meta:
        model=Post
        fields=[
            'title',
            'category',
            'description',
            'tag',
            'source',
            'person',
            'image',
            

        ]
class CommentForm(forms.ModelForm):

    class Meta:
        model=Comment
        fields=[
            'name',
            'comment',

        ]
                
class ContactForm(forms.ModelForm):
     class Meta:
          model=Contact
          fields=[
              'ad',
              'soyad',
              'sual',
          ]
class EmailForm(forms.ModelForm):
    class Meta:
        model=Subscribe
        fields=[
            'mail'
        ]