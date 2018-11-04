from .models import ElanComment,Elan
from django import forms

class CommentForm(forms.ModelForm):

    class Meta:
        model=ElanComment
        fields=[
            'name',
            'comment',

        ]
class ElanForm(forms.ModelForm):

    class Meta:
        model=Elan
        fields=[
            'elanTitle',
            'elanDescription',
            'elanPrice',
            'owner',
            'ownerPhone',
            'ownerMail',
            'ownerCity',
            'itemCategory',
            'image'
        ]                
