from django.db import models
from UserManagement.models import Profile
# Create your models here.


class Owner(models.Model):
    no_of_property = models.CharField(max_length=100)
    Type = models.ForeignKey(Profile,on_delete=models.CASCADE)



def __str__(self):
        return '%s %s' % (self.Type.First_Name, self.Type.Last_Name)
