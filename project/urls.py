"""project URL Configuration

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
from django.urls import path, include
from newapp import views
from newapp import views as newapp_view
from django.contrib.auth import views as auth
from rest_framework.authtoken import views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('newapp.urls')),
    path('api-token-auth/',views.obtain_auth_token,name='api-tokn-auth'),

    # get user id

    path('getuideveryone/', newapp_view.useridList),

    path('device/',newapp_view.device_list),
    path('setupthings/',newapp_view.setup_list),
    path('findhealth/',newapp_view.health_list),
    path('ssidpassword/',newapp_view.ssidpass_list),

    
    # profile picture
    path('profilepicture/',newapp_view.profoto),

    # friends in need friend indeed

    path('friendsuaccess/', newapp_view.friendsuaccess),
    path('friendtoaddlist/', newapp_view.friendtoaddList),
]
