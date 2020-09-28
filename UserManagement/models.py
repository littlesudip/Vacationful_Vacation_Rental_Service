from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):

    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=200)
    NID_id=models.IntegerField(blank=True,null=True)
    address=models.CharField(max_length=300)
    contact_no=models.IntegerField(blank=True,null=True)
    profile_picture = models.ImageField(upload_to='images/pro_pic', blank=True, null=True,default='users/pro_pics/default.jpg')
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
