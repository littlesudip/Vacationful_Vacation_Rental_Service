"""Vacationful URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from PropertyManagement import views as property_views
from PropertyManagement.views import showallproperty
from UserManagement import  views as user_views
from django.urls import path,include
from Booking import views as booking_views
from Traveller import views as traveller_views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', user_views.viewprofile),
    path('admin/', admin.site.urls),
    path('addproperty/',property_views.addproperty,name='addproperty' ),
    path('showproperty/', property_views.showallproperty,name='showproperty'),
    path('register/', user_views.register, name='register'),
    path('createprofile/',user_views.createprofile,name='createprofile'),
    path('viewprofile/',user_views.viewprofile,name='viewprofile'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('showbookinglist/',booking_views.showbookinglist,name='showbookinglist'),
    path('addbookinginfo/',booking_views.addbookinginfo,name='addbookinginfo'),
    path('showtravellerlist/',traveller_views.showtravellerlist,name='showtravellerlist'),
    path('addbookinginfo/',traveller_views.addtravellerinfo,name='addtravellerinfo'),
    path('homepage/', property_views.homepage, name='property_list'),
    path('homepage/<int:property_id>', property_views.showDetails, name='detail_view'),
    # path('showdetails/<int:property_id>', property_views.showDetails, name='detail_view'),


]

if settings.DEBUG == True:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
