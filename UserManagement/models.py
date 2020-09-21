from django.db import models

# Create your models here.
class User(models.Model):
    user_id=models.IntegerField()
    use_type=models.CharField(max_length=100)
    nid_id=models.IntegerField(blank=True,null=True)
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=200)
    address=models.CharField(max_length=300)
    contact_no=models.IntegerField(blank=True,null=True)
