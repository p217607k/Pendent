from django.urls import path,include
from django.conf import settings
from newapp import views


urlpatterns = [

    path('', views.index, name='homepage'),
    path('register',views.register_flutter,name='flutter-register'),
    path('ckeckingmail',views.checkemail,name='email-check'),
    path('ckeckingpassword',views.checkpassword,name='pass-check'),
    path('ssidpassword',views.SSID_Password,name='ssid-and-password'),
    
]