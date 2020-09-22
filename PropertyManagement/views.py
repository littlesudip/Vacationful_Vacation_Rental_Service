from django.shortcuts import render
from .models import Property
# Create your views here.



def allproperty(request):

    listproperty = Property.objects.all()

    context = {""
               "all_property": listproperty
               }

    return render(request, 'Property/allproperty.html',context)



def addproperty(request):

    message = ""
    form= PropertyForm()
    if request.method == "POST":

        form = PropertyForm(request.POST)
    message = "Invalid input. Please try again!"
    if form.is_valid():
        form.save()
        message = "Property is inserted to Database. You can insert a new property"
        form = PropertyForm()
    context = {
        'form': form,
        'message' : message
    }
    return render(request, 'Property/addproperty.html' ,context)
