from rest_framework import serializers
from django.contrib.auth.models import User
from drf_braces.serializers.form_serializer import FormSerializer
from myapp.forms import UserRegisterForm
# from myapp.models import place_type,floor,room,device,deviceStatus,emergencyNumber,sensors


class userSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =  '__all__'

class user_register(FormSerializer):
    class Meta(object):
        form = UserRegisterForm