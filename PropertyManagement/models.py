from django.db import models

# Create your models here.
class Property(models.Model):

    property_name= models.CharField(max_length=200)
    property_location=models.CharField(max_length=200)
    property_details=models.CharField(max_length=200)
    property_pricing= models.FloatField(blank=True,null=True)