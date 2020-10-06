from django.shortcuts import render, redirect

from Owner.models import Owner
from Traveller.models import Traveller
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required



def register(request):
    form = UserCreationForm()
    form1 = ProfileForm(request.POST, request.FILES)

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            if form1.is_valid():
                profile = form1.save(commit=False)
                profile.user = user
                profile = profile.save()
                r = int(form1.cleaned_data.get('Role'))
                if r == 1:
                    print("OWNER",r)
                    owner = Owner(user=user)
                    owner.save()
                if r == 2:
                    print("TRAVELLER",r)
                    traveller = Traveller(user=user)
                    traveller.save()
            return render(request, 'profile/viewprofile.html')

    context = {
        'form': form,
        'form1': form1
    }
    return render(request, 'user/register.html', context)


# Create your views here.
@login_required()
def viewprofile(request):
    if request.user.is_authenticated:
        ProfileList = Profile.objects.filter(user=request.user)
        owner = Owner.objects.filter(user=request.user)
        if owner:
            context = {
            'Profiles': ProfileList,
            "owner": True,
            }
        else:
            context = {
            'Profiles': ProfileList,
            "traveller": True,
            }
    return render(request, 'profile/viewprofile.html', context)


@login_required()
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
            return redirect('viewprofile')

            message = "Profile is inserted to DB. You can insert a new Profile now"
            form = ProfileForm()

    context = {
        'form': form,
        'message': message
    }
    return render(request, 'profile/createprofile.html', context)
