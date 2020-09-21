from django.shortcuts import render

# Create your views here.
def showUserInfo(request):
    return render(request,'UserManagement/showuserinfo.html')