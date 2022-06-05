from django import forms
from .models import *

class RegForm(forms.ModelForm):
    class Meta:
        model  = Person
        fields = '__all__'



