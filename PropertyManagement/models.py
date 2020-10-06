from django.db import models

# Create your models here.
from Owner.models import Owner


class Property(models.Model):

    property_name= models.CharField(max_length=200)
    owner_id= models.ForeignKey(Owner,on_delete=models.CASCADE,default=1)
    property_type=models.CharField(max_length=200)
    property_location = models.CharField(max_length=200)
    no_of_rooms = models.IntegerField(blank=True, null=True)
    property_description = models.CharField(max_length=200)
    property_pricing= models.FloatField(blank=True,null=True)
    legal_documents= models.ImageField(upload_to='images/property',blank=True, default='images/property/land-documents.jpg')
    property_picture = models.ImageField(upload_to='images/property',blank=True, default='images/property/house.jpg')

    def __str__(self):
        return self.property_name
