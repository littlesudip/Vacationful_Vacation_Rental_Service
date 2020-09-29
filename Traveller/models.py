from django.db import models
from UserManagement.models import Profile
# Create your models here.

class Traveller(models.Model):
    user = models.ForeignKey(Profile,on_delete=models.CASCADE)

    def __str__(self):
        return (self.user.Full_name)
