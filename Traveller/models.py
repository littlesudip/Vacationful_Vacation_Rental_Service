from django.contrib.auth.models import User
from django.db import models
from UserManagement.models import Profile
from PropertyManagement.models import Property



# Create your models here.

class Traveller(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.user.username
