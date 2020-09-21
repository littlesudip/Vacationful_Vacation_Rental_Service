from django.db imports models
from PropertyManagement import Property
from Traveller import User_ID

# Create your models here.

class BookingManagement(models.Model):
	Property_Info = models.ForeignKey(Property, on_delete=models.CASCADE, default=1, null=True)
	Info = models.ForeignKey(Traveller, on_delete=models.CASCADE, default=1, null=True)

