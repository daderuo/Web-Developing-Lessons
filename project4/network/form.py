from typing import Text
from django.forms import ModelForm,Textarea, TextInput, NumberInput, FileInput, ModelChoiceField
from django.forms.widgets import Select
from .models import *
from django import forms

class CreatePostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ['date_time']
        widgets = {
            'text': Textarea(attrs={'id': 'NewPostText','cols':'100%','rows':'3'})
        }  