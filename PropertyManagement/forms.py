from django import forms
from .models import Property
from django.forms import ModelForm

class PropertyForm(forms.ModelForm):
    class Meta:
        model= Property
        fields = '__all__'