from django.contrib import admin
from .models import Traveller,Booking,Property


# Register your models here.
admin.site.register([Traveller,Booking,Property])