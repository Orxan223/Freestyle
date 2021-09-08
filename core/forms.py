from django.forms import ModelForm
from .models import *


class IndexForm(ModelForm):
    
    class Meta:
        model = Index
        fields = 'title','text','count','is_active'

