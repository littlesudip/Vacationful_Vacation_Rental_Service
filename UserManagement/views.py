from django.shortcuts import render
from .forms import CreateUserCreationForm
from .models import User
# Create your views here.

def showuserinfo(request):

    member = User.objects.all()

    context = {"all_user": member
               }
    return render(request,"UserManagement/showuserinfo.html",context)











