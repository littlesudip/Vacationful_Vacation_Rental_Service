from django.shortcuts import render
from .forms import forms
from .models import User
from django.shortcuts import render

# Create your views here.
from UserManagement.forms import infoForm

def showuserinfo(request):

    member = User.objects.all()

    context = {"all_user": member
               }
    return render(request,"UserManagement/showuserinfo.html",context)



def inserinfo(request):

    message = ""
    form= infoForm()
    if request.method == "POST":

        form = infoForm(request.POST)
    message = "Invalid input. Please try again!"
    if form.is_valid():
        form.save()
        message = "Thank You"
        form = infoForm()
    context = {
        'form': form,
        'message' : message
    }
    return render(request, 'User/inserinfo.html' ,context)





