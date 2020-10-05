from django import forms
from .models import Profile
from django.forms import ModelForm





class ProfileForm(forms.ModelForm):
    Role = forms.ChoiceField(choices=(('1','Owner'),('2','Traveller')))
    class Meta:
        model=Profile
        fields=('Full_name','Email','Address','Contact_No','Profile_Picture','NID_No','NID_Front','NID_Back')