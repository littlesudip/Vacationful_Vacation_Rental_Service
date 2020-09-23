from django.shortcuts import render

from .forms import infoForm
from .models import User
# Create your views here.


def showuserinfo(request):

    member = User.objects.all()

    context = {"all_user": member
               }
    return render(request,"UserManagement/showuserinfo.html",context)



def insertinfo(request):
    message = " "
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
    return render(request,'UserManagement/insertinfo.html',context)





