from django.shortcuts import render
from .forms import PropertyForm
from .models import Property
from Owner.models import Owner
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Property
from .forms import PropertyForm
from Booking.forms import BookingForm
from Traveller.models import Traveller
from django.contrib.auth.decorators import login_required
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
        form = PropertyForm(request.POST,request.FILES)
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


def homepage(request):
    if request.user.is_authenticated:
        owner = Owner.objects.filter (user = request.user )

    property = Property.objects.all()

    if request.method == 'POST':
        name = Property.objects.filter(name__icontains = request.POST['search'])
        category = Property.objects.filter(category__icontains = request.POST['search'])
        description = Property.objects.filter(description__icontains = request.POST['search'])

        property = name | category | description # C = A U B set operation

    user_count = User.objects.count()
    product_count = Property.objects.count()

    if owner:
        context = {
        'property' : property,
        'u_c' : user_count,
        'p_c' : product_count,
        "owner": True,
        }

    else:
        context = {
            'property': property,
            'u_c': user_count,
            'p_c': product_count,
            "traveller": True,
        }

    return render(request, 'Property/homepage.html', context)

def showDetails(request, property_id):
    if request.user.is_authenticated:
        traveller = Traveller.objects.filter (user = request.user )
        if traveller:
            form = BookingForm()
            traveller = Traveller.objects.filter(user=request.user)
            searched_property = get_object_or_404(Property, id=property_id)

            if request.method == "POST":
                form = BookingForm(request.POST)
                if form.is_valid():
                    booking = form.save(commit=False)
                    property = Property.objects.get(id=int(request.POST.get("p_id")))
                    booking.Property_ID = property
                    booking.Traveller_ID = traveller[0]
                    booking.save()

            context = {
                'search': searched_property,
                'form': form,
                "traveller": True,
            }
    return render(request, 'Property/detail_property_view.html', context)





