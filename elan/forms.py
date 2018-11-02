from .models import ElanComment
from django import forms

class CommentForm(forms.ModelForm):

    class Meta:
        model=ElanComment
        fields=[
            'name',
            'comment',

        ]
                