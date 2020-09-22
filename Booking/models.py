from django.db import models
from PropertyManagement.models import Property
from UserManagement.models import Traveller, Owner


# Create your models here.

class BookingManagement(models.Model):
    traveller = models.ForeignKey(Traveller, on_delete=models.CASCADE, default=1, null=True)

    def __str__(self):
        return self.traveller