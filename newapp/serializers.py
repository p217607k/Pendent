from rest_framework import serializers
from django.contrib.auth.models import User
from drf_braces.serializers.form_serializer import FormSerializer
from newapp.forms import UserRegisterForm
from newapp.models import device, setup
# from myapp.models import place_type,floor,room,device,deviceStatus,emergencyNumber,sensors

class deviceSerializers(serializers.ModelSerializer):
    class Meta:
        model = device
        fields = ('id','d_id', 'd_name')

class setupSerializers(serializers.ModelSerializer):
    class Meta:
        model = setup
        fields = ('id','trigger','color','ring','message')
        depth = 1


class userSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =  '__all__'

class user_register(FormSerializer):
    class Meta(object):
        form = UserRegisterForm