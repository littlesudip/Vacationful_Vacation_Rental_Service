from django.shortcuts import render
from .models import Profile
from .forms import ProfileForm


# Create your views here.
def showProfile(request):

    ProfileList= Profile.objects.all()
    context = {
        'Profiles': ProfileList
    }
    return render(request, 'profile/viewProfile.html', context)





def createProfile(request):
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
    return render(request, 'profile/createProfile.html', context)
