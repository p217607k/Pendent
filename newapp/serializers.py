from rest_framework import serializers
from django.contrib.auth.models import User
from drf_braces.serializers.form_serializer import FormSerializer
from newapp.forms import UserRegisterForm
from newapp.models import device, setup, healthrecord, ssidPassword
# from myapp.models import place_type,floor,room,device,deviceStatus,emergencyNumber,sensors

class deviceSerializers(serializers.ModelSerializer):
    class Meta:
        model = device
        # fields = ('d_id', 'd_name')
        fields = '__all__'

class setupSerializers(serializers.ModelSerializer):
    class Meta:
        model = setup
        fields = ('id','trigger','color','ring','message')
        depth = 1


# class healthSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = health
#         fields = ('H1sensor','H2sensor','H3sensor','H4sensor')

class recordhealthSerializers(serializers.ModelSerializer):
    class Meta:
        model = healthrecord
        # fields = ('d_id', 'd_name')
        fields = '__all__'

class userSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =  '__all__'

class user_register(FormSerializer):
    class Meta(object):
        form = UserRegisterForm

class ssidPasswordSerializers(serializers.ModelSerializer):
    class Meta(object):
        model = ssidPassword
        fields = ('ssid','password')
        depth = 3
        