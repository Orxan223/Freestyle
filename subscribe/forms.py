from django.forms import widgets
from .models import Subscribe
from django import forms

class SubscribeForms(forms.ModelForm):
    
    class Meta:
        model = Subscribe
        fields = ['email']

        widgets = {
            'email': forms.EmailInput(attrs={"class":"form--control","placeholder":('Email')})
        }