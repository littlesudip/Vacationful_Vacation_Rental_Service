from django.shortcuts import render
from .forms import BookingForm
from .models import Booking
# Create your views here.

def showbookinglist(request):

    bookinglist = Booking.objects.all()

    context = {
               "bookinginfo": bookinglist
               }
    return render(request, 'booking/showbookinglist.html',context)

def addbookinginfo(request):

    message = ""
    form= BookingForm()
    if request.method == "POST":

        form = BookingForm(request.POST)

    if form.is_valid():
        form.save()
        message = "Your Booking Details is inserted to Database. You can insert a new property"
        form = BookingForm()
    context = {
        'form': form,
        'message' : message
    }
    return render(request, 'booking/addbookinginfo.html' ,context)