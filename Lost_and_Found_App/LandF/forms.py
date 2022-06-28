# from django.db import models  
# from django.forms import fields  
from .models import Lost  
from django import forms  

class LostForm(forms.ModelForm):
    class Meta:
        model = Lost
        fields = '__all__'

