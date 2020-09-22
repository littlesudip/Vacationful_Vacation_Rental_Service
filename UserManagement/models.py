from django.db import models

# Create your models here.




class User(models.Model):

    NID_ID = models.IntegerField(blank=True,null=True)
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=200)
    address=models.CharField(max_length=300)
    contact_no=models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.name

class Traveller(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, null=True)
    travelling_area = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Owner(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, null=True)
    number_of_property=models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.name