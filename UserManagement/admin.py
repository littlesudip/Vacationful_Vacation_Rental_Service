from django.contrib import admin
from .models import User, Traveller

# Register your models here.
admin.site.register([User, Traveller])
