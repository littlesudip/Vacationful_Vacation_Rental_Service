


from django.shortcuts import render

# Create your views here.
from PropertyManagement.forms import PropertyForm


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
