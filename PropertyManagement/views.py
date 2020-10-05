from django.shortcuts import render
from .forms import PropertyForm
from .models import Property
from Owner.models import Owner
# Create your views here.

def showallproperty(request):

    listproperty = Property.objects.filter(owner_id__user=request.user)
    
    context = {
               "all_property": listproperty,
                "owner": True,
                "traveller":False,
               }
    return render(request, 'Property/showallproperty.html',context)


def addproperty(request):

    message = ""
    form= PropertyForm()
    if request.method == "POST":
        form = PropertyForm(request.POST)
        if form.is_valid():
            owner = Owner.objects.get(user=request.user)
            ins= form.save(commit=False)
            ins.owner_id = owner
            ins.save()
            message = "Your Property is inserted Sucessfully. You can insert a new Property"
    form = PropertyForm()
    context = {
        "owner": True,
        'form': form,
        'message' : message
    }
    return render(request, 'Property/addproperty.html' ,context)