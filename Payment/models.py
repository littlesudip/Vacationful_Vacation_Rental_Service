from django.db import models
from PropertyManagement.models import Property
from UserManagement.models import Traveller

# Create your models here.
class PaymentManagement(models.Model):
    property=models.ForeignKey(Property, on_delete=models.CASCADE, default=1, null=True)
    travel= models.ForeignKey(Traveller, on_delete=models.CASCADE, default=1, null=True)
