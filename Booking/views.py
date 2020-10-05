from django.shortcuts import render
from .forms import BookingForm
from .models import Booking
from Traveller.models import Traveller
# Create your views here.

def showbookinglist(request):

    bookinglist = Booking.objects.all()

    context = {
                "traveller":True,
               "bookinginfo": bookinglist
               }
    return render(request, 'booking/showbookinglist.html',context)

def addbookinginfo(request):
    traveller = Traveller.objects.get(user=request.user)
    message = ""
    form= BookingForm()
    if traveller:
        if request.method == "POST":

            form = BookingForm(request.POST)

            if form.is_valid():
                traveller = Traveller.objects.get(user=request.user)
                ins=form.save(commit=False)
                ins.Traveller_ID= traveller
                ins.save()
                message = "Your Booking Details is inserted to Database. You can insert a new property"
        form = BookingForm()
        context = {
            "traveller": True,
            'form': form,
            'message' : message
            }
        return render(request, 'booking/addbookinginfo.html' ,context)