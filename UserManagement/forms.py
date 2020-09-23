from django import forms
from .models import User
from django.forms import ModelForm

class infoForm(forms.ModelForm):
    class Meta:
        model=User
        fields= '__all__'
