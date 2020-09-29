from django.db import models
from Traveller.models import Traveller


# Create your models here.

class Booking(models.Model):
    Checkin_Date = models.CharField(max_length=100)
    Checkin_Time = models.CharField(max_length=100)
    Checkout_Date = models.CharField(max_length=100)
    Checkout_time = models.CharField(max_length=100)
    No_of_Guests = models.IntegerField(blank=True, null=True)
    traveller_Info = models.ForeignKey(Traveller,on_delete=models.CASCADE)


def __str__(self):
        return self.traveller_Info.tarvelling_area



