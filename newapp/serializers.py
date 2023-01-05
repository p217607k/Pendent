from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from drf_braces.serializers.form_serializer import FormSerializer
from newapp.forms import UserRegisterForm
from newapp.models import *
# from myapp.models import place_type,floor,room,device,deviceStatus,emergencyNumber,sensors

class userlogingetdataSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email','first_name',)
##
class roomSerializers(serializers.ModelSerializer):
    class Meta:
        model =Message
        fields = '__all__'
###
class getuseremailSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email',)

class getusernamewithemailSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','first_name',)

# class partneralldataSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = partner
#         fields = '__all__'

class deviceSerializers(serializers.ModelSerializer):
    class Meta:
        model = device
        # fields = ('d_id', 'd_name')
        fields = '__all__'

class allsetupSerializers(serializers.ModelSerializer):
    class Meta:
        model = setup
        # fields = ('d_id', 'd_name')
        fields = '__all__'


class setuppSerializers(serializers.ModelSerializer):
    class Meta:
        model = setup
        fields = '__all__'


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
        fields = ('ssid1','password1','ssid2','password2','ssid3','password3',)

class userprofileimagesSerializers(serializers.ModelSerializer):
    class Meta:
        model = userimages
        fields = '__all__'


class friendaddSerializers(serializers.ModelSerializer):
    class Meta:
        model = friendadd
        fields = ('emailtest',)

class friendaccessSerializers(serializers.ModelSerializer):
    class Meta:
        model = friendadd
        fields = '__all__'

class familyaddaccessSerializers(serializers.ModelSerializer):
    class Meta:
        model = familymanaccess
        fields = '__all__'


class friendtoaccessSerializers(serializers.ModelSerializer):
    class Meta:
        model = friendtoaccess
        fields = '__all__'

# class friendtoaccessgetSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = friendtoaccess
#         fields = ('name','email')


class emernumberSerializers(serializers.ModelSerializer):
    class Meta:
        model = emergencyNumber
        fields = '__all__'


class ssidPasswordSerializers(serializers.ModelSerializer):
    class Meta:
        model = ssidPassword
        fields = '__all__'
        
class proimgSerializers(serializers.ModelSerializer):
    class Meta:
        model = userimages
        fields = '__all__'

class allemailsSerializers(serializers.ModelSerializer):
    class Meta:
        model = allEmail
        fields = '__all__'


class partnersSerializers(serializers.ModelSerializer):
    class Meta:
        model = partner
        fields = '__all__'

class recivedsetupSerializers(serializers.ModelSerializer):
    class Meta:
        model = receivedsetup
        fields = '__all__'


class allemailsSerializers(serializers.ModelSerializer):
    class Meta:
        model = allEmail
        fields = '__all__'

class allSOSSerializers(serializers.ModelSerializer):
    class Meta:
        model = SOS
        fields = '__all__'