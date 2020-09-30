from django.db import models
from Traveller.models import Traveller
from PropertyManagement.models import Property


# Create your models here.

class Booking(models.Model):
    Traveller_ID= models.ForeignKey(Traveller,on_delete=models.CASCADE,default=1)
    Property_ID= models.ForeignKey(Property,on_delete=models.CASCADE,default=1)
    Checkin_Date = models.CharField(max_length=100)
    Checkin_Time = models.CharField(max_length=100)
    Checkout_Date = models.CharField(max_length=100)
    Checkout_time = models.CharField(max_length=100)
    No_of_Guests = models.IntegerField(blank=True, null=True)
    

def __str__(self):
        return self.traveller_Info.Full_Name



