from django.shortcuts import render
from .forms import forms
from .models import User
# Create your views here.

def showuserinfo(request):

    member = User.objects.all()

    context = {"all_user": member
               }
    return render(request,"UserManagement/showuserinfo.html",context)

def insertinfo(request):
    form = forms()

    context = {
            'form' : form
    }
    return render(request, "UserManagement/insertinfo.html", context)









