from django.contrib.auth.forms import forms
from django.contrib.auth.models import User

class infoForm(forms.ModelForm):
    class Meta:
        model=User
        fields= '__all__'
