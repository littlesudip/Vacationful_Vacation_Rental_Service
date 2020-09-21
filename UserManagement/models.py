from django.db import models

# Create your models here.
class Address(models.Model):
    house_no = models.IntegerField(blank=True,null=True,default="")
    street_address = models.CharField(max_length= 200)
    postal_address = models.CharField(max_length = 200)
    post_code = models.CharField(max_length=20)
    city = models.CharField(max_length = 20)

def __str__(self):
    return str(self.house_no)+""+self.city

class User(models.Model):
    user_type = models.CharField(max_length=100)
    nid_id = models.IntegerField(blank=True,null=True)
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=200)
    address=models.CharField(max_length=300)
    contact_no=models.IntegerField(blank=True,null=True)


def __str__(self):
    return self.name



