from django.shortcuts import render
from .models import Property
# Create your views here.


def allproperty(request):

    listproperty = Property.objects.all()

    context = {""
               "all_property": listproperty
               }

    return render(request, 'Property/allproperty.html',context)
