from django import forms
from .models import Booking
from django.forms import ModelForm

class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields='__all__'