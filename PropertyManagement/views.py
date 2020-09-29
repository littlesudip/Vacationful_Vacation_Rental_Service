from django.shortcuts import render
from .forms import PropertyForm
from .models import Property
# Create your views here.

def showallproperty(request):

    listproperty = Property.objects.all()

    context = {
               "all_property": listproperty
               }
    return render(request, 'Property/showallproperty.html',context)


def addproperty(request):

    message = ""
    form= PropertyForm()
    if request.method == "POST":

        form = PropertyForm(request.POST)

    if form.is_valid():
        form.save()
        message = "Property is inserted to Database. You can insert a new property"
        form = PropertyForm()
    context = {
        'form': form,
        'message' : message
    }
    return render(request, 'Property/addproperty.html' ,context)