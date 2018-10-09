from django import forms
from .models import Post, Comment, Contact

class PostForm(forms.ModelForm):

    class Meta:
        model=Post
        fields=[
            'title',
            'description',
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
