from django.urls import path,include
from django.conf import settings
from newapp import views
from newapp.views import(
	send_friend_request,
	friend_requests,
	accept_friend_request,
	remove_friend,
	decline_friend_request,
	cancel_friend_request,

)

app_name = 'newapp'


urlpatterns = [

    path('', views.index, name='homepage'),
    path('registertodent',views.register_flutter,name='flutter-register'),
    path('ckeckingmail',views.checkemail,name='email-check'),
    path('ckeckingpassword',views.checkpassword,name='pass-check'),
    
]