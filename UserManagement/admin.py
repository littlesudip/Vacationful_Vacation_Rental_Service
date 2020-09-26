from django.contrib import admin
from .models import User, Traveller,Owner

# Register your models here.
admin.site.register([User, Traveller,Owner])
