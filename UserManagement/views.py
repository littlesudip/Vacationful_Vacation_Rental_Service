from django.shortcuts import render
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth.forms import UserCreationForm

def register(request):

    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context ={
        'form' : form
    }
    return render(request, 'user/register.html', context)




# Create your views here.
def viewprofile(request):

    ProfileList= Profile.objects.all()
    context = {
        'Profiles': ProfileList
    }
    return render(request, 'profile/viewprofile.html', context)

def createprofile(request):
    message = ""
    form = ProfileForm()

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        message = "Invalid input. Please try again!"
        if form.is_valid():

            profile = form.save(commit=False)

            profile.user = request.user

            profile.save()

            message = "Profile is inserted to DB. You can insert a new Profile now"
            form = ProfileForm()

    context = {
        'form' : form,
        'message' : message
    }
    return render(request, 'profile/createprofile.html', context)