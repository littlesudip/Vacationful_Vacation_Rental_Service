from django.db import models
from UserManagement.models import Profile
# Create your models here.

class Traveller(models.Model):
    travelling_area = models.CharField(max_length=1000)
    User_Type = models.ForeignKey(Profile,on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.User_Type.First_Name, self.User_Type.Last_Name)
