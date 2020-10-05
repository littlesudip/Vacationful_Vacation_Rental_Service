from django import forms
from .models import Booking
from django.forms import ModelForm


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('Property_ID', 'Checkin_Date', 'Checkin_Time', 'Checkout_Date', 'Checkout_time', 'No_of_Guests')
