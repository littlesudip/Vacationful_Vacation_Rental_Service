from django.shortcuts import render
from .forms import PropertyForm
from .models import Property
from Owner.models import Owner
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Property
from .forms import PropertyForm
from django.contrib.auth.decorators import login_required
# Create your views here.




def showallproperty(request):

    listproperty = Property.objects.filter(owner_id__user=request.user)
    
    context = {
               "all_property": listproperty,
                "owner": True,
                "traveller":True,
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


def homepage(request):

    property = Property.objects.all()


    if request.method == 'POST':
        name = Property.objects.filter(name__icontains = request.POST['search'])
        category = Property.objects.filter(category__icontains = request.POST['search'])
        description = Property.objects.filter(description__icontains = request.POST['search'])

        property = name | category | description # C = A U B set operation

    user_count = User.objects.count()
    product_count = Property.objects.count()

    context = {
        'property' : property,
        'u_c' : user_count,
        'p_c' : product_count
    }
    return render(request, 'Property/homepage.html', context)

def showDetails(request, property_id):


    searched_property = get_object_or_404(Property, id=property_id)


    form = ReviewForm()


    if request.method == "POST":
        form = ReviewForm(request.POST)


        if form.is_valid:
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()


            searched_property.reviews.add(instance)
            searched_property.save()


    context = {
        'search': searched_property,
        'form': form
    }
    return render(request, 'Property/detail_property_view.html', context)








def showDetails2(request, product_id):


    #searched_product = get_object_or_404(Product, id=product_id)


    #searched_product = Product.objects.get(id=product_id) #sure one return
    #print(searched_product)


    searched_product = Property.objects.filter(id=property_id)  # many return


    #searched_product = get_object_or_404(Product, id=product_id)
    #print(searched_product)






    if len(searched_property) == 0:
        does_exists = False
        context = {
            'does_exists': does_exists,
        }
    else:
        does_exists = True
        search = searched_property[0]
        context = {
            'does_exists': does_exists,
            'search': search
        }


    return render(request, 'Property/detail_property_view.html', context)



