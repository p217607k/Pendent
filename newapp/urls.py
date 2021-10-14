from django.urls import path,include
from django.conf import settings
from newapp import views

app_name = 'newapp'


urlpatterns = [

    path('', views.index, name='homepage'),
    path('registertodent',views.register_flutter,name='flutter-register'),
    path('ckeckingmail',views.checkemail,name='email-check'),
    path('ckeckingpassword',views.checkpassword,name='pass-check'),
    
]