from django import forms
from .models import Traveller
from django.forms import ModelForm


class TravellerForm(forms.ModelForm):
    class Meta:
        model = Traveller
        fields = ('Property_name',)
