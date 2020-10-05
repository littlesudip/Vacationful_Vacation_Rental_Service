from django.db import models
from UserManagement.models import Profile
from django.contrib.auth.models import User
# Create your models here.

class Owner(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, default=1)

    def __str__(self):
        return (self.user.username)