from django.shortcuts import render
from .forms import TravellerForm
from Traveller.models import Traveller
# Create your views here.

def showtravellerlist(request):

    showtravellerlist = Traveller.objects.all()

    context = {
                "traveller":True,
               "travellerinfo": showtravellerlist()
               }
    return render(request, 'booking/showtravellerlist.html',context)

def addtravellerinfo(request):
    traveller = Traveller.objects.get(user=request.user)
    message = ""
    form= TravellerForm()
    if traveller:
        if request.method == "POST":

            form = TravellerForm(request.POST)

            if form.is_valid():
                traveller = Traveller.objects.get(user=request.user)
                ins=form.save(commit=False)
                ins.Traveller_ID= traveller
                ins.save()
                message = "Your Details is inserted to Database."
        form = TravellerForm()
        context = {
            "traveller": True,
            'form': form,
            'message' : message
            }
        return render(request, 'traveller/addtravellerinfo.html' ,context)