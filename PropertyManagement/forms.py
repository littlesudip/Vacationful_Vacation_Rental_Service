from django import forms
from .models import Property
from django.forms import ModelForm


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ('property_name', 'property_type', 'property_location', 'no_of_rooms', 'property_description',
                  'property_pricing', 'legal_documents', 'property_picture')
