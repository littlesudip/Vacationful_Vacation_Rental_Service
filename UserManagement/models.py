from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    Full_name = models.CharField(max_length=100, blank=True, null=True, )
    Email = models.EmailField(max_length=200, blank=True, null=True, )
    Address = models.CharField(max_length=300, blank=True, null=True, default="")
    Contact_No = models.IntegerField(blank=True, null=True, default="")
    Profile_Picture = models.ImageField(upload_to='images/pro_pic', blank=True, null=True,
                                        default='users/pro_pics/default.jpg')
    NID_No = models.IntegerField(blank=True, null=True, default="")
    NID_Front = models.ImageField(upload_to='images/idcard', blank=True, null=True, default='images/idcard/front.jpg')
    NID_Back = models.ImageField(upload_to='images/idcard', blank=True, null=True, default='images/idcard/back.jpg')
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, )

    def __str__(self):
        return self.user.username
