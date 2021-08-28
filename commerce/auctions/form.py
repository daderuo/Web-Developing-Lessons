from typing import Text
from django.forms import ModelForm,Textarea, TextInput, NumberInput, FileInput, ModelChoiceField
from django.forms.widgets import Select
from .models import *
from django import forms


class CreateListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = '__all__'
        widgets = {
            'title': TextInput(attrs={'class':'form-control form-control-sm'}),
            'description': Textarea(attrs={'class':'form-control form-control-sm'}),
            'price': NumberInput(attrs={'class':'form-control'}),
            'image': FileInput(attrs={'class':'form-control'}),
            'category': Select(attrs={'class':'form-control'})
        }  