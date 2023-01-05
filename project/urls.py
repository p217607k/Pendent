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
    path('roomchat/', newapp_view.roomdetailList),
    #user data
    path('getthedataofuser/',newapp_view.userdataList),#with user id
    path('getthenameofuserwemail/',newapp_view.nameWemail),#with email id
    path('getthenameofuserwusername/',newapp_view.nameWusername),#with username
    
    # get all emails
    path('getallemailswithuser/', newapp_view.allemail),
    path('roomchat/', newapp_view.roomdetailList),


    # get user id
    path('getuideveryone/', newapp_view.useridList),

    path('device/',newapp_view.device_list),

    #schedule setup
    path('setupthings/',newapp_view.setup_list),
    #receive setup
    path('receivethesetup/', newapp_view.setup_received),

    path('findhealth/',newapp_view.health_list),
    path('ssidpassword/',newapp_view.ssidpass_list),

    
    # profile picture
    path('profilepicture/',newapp_view.profileimage),

    # emer number & ssid pass
    path('addemernumbers/', newapp_view.emerNumber),
    path('enterallthessidpasswords/', newapp_view.ssidList),

    # friends in need friend indeed
    path('friendsuaccess/', newapp_view.friendsuaccess),
    path('friendtoaddlist/', newapp_view.friendtoaddList),
    #accept requests
    path('acceptingfriendtoaddlist/', newapp_view.acceptingfriendtoaddList),

    # partner connection
    path('connecttopartner/', newapp_view.connectpartner),
    # search friend requests with emails
    path('searchfrequests/', newapp_view.searchrequests),

    #schedule setup  ############ URL ############
    path('schedulereceived', newapp_view.scheduleSetup),

    #### family connections 
    path('addfamilymenber/', newapp_view.connectmyfamily),
    #### accepting request and get d_id too for getting health data
    path('acceptgetfamilymenber/', newapp_view.searchrequestsfamily),

    #### SOS api
    path('addsostosend/', newapp_view.connectmySOS),
]


admin.site.site_header = 'Pendent Database'