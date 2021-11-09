from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth.models import User
from rest_framework import response
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from .forms import *
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from newapp.serializers import *
import json
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework import status
# from .models import employees
# from .serializers import employeesSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AND, IsAuthenticated
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,password_validation
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth.models import User
from rest_framework.decorators import authentication_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework import serializers
from rest_framework import status
import random, math
from newapp.models import *
from datetime import date
import os
from django.conf import settings
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import permissions
import http.client
import ast
from requests.api import request
import requests

conn = http.client.HTTPConnection("2factor.in")

@api_view(["GET"])
# @permission_classes([IsAuthenticated])
def useridList(request):
    if request.method=="GET":
        current_user = request.user
        print(current_user.id)
        return Response(current_user.id)

def room(request, room_name):
  username = request.GET.get('username', 'Anonymous')

  return render(request, 'chat/room.html', {'room_name': room_name, 'username': username})

# Create your views here.

@api_view(["GET"])
def userdataList(request):
    if request.method=="GET":
        device_data = User.objects.filter(id=request.GET['id'])
        nameJson = userlogingetdataSerializers(device_data, many=True)
        # return Response(nameJson.data)
        dd = list(nameJson.data)[0]
        print(dd)
        return Response(dd)


@api_view(["GET"])
def nameWemail(request):
    if request.method == 'GET':
        data1 = User.objects.filter(email = request.GET['email'])
        dataJson = getusernamewithemailSerializers(data1, many=True)
        return Response(dataJson.data)
        # dd = dataJson.data[:]
        # return Response(dd[0])

## get all emails
@api_view(["GET"])
def allemail(request):
    if request.method == 'GET':
        data1 = allEmail.objects.filter(email = request.GET['email'])
        dataJson = allemailsSerializers(data1, many=True)
        return Response(dataJson.data)
        # dd = dataJson.data[:]
        # return Response(dd[0])




def index(request):
    # channel_layer = get_channel_layer()
    # async_to_sync(channel_layer.group_send)(
    #     't_cons_group', {
    #         'type': 'send'
    #     }
    # )
    items = []
        # current_user = request.user
        # uuiid = current_user.id
    a = healthrecord.objects.all()
    tagsJson = recordhealthSerializers(a, many=True)
    for i in range(len(tagsJson.data)):
        tag = tagsJson.data[i]

        print(tag)
        
        # listname = tagsJson.data[i]["listname"]
        # userid = tagsJson.data[i]["userid"]
        # if tag == data1 or data1=="All":
        #     if userid == current_user.id:
                # if listname == data2:
        items.append(tag)
    print(items)
    context = {
        'items' : items,
    }
        
    # data = healthrecord.objects.all()
    # print(list(data)[0])
    # stu = {
    #     "hre": data
    # }

    # print(dict(stu))
    return render(request, "ind.html", context)
    # return render(request, 'index.html')


@csrf_exempt
@renderer_classes((JSONRenderer))
def register_flutter(request):
    print("1st")
    form = UserRegisterForm(request.POST)
    # print(request.POST)
    # print(form)
    if form.is_valid():
        form.save()
        # print(form.email)
        print((form.data["email"]))
        e  = form.data["email"]
        # em = User(email = e)
        # print("1" , em)
        d = allEmail.objects.create(email = e)
        d.save()
        u = form.data["username"]
        # u = User(username = u)
        d1 = allusernames.objects.create(username = u)
        d1.save()
        print("I am save.")
        return JsonResponse({"Registration":"Done"})
    else :
        # return JsonResponse({"Password is too similar"})
        print(form.errors.as_json())
        # return JsonResponse({"Password is too similar"})
        # return Response("data updated", status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR ,data=form.errors.as_json())
        # print("pass is too similar")
        # return JsonResponse({"Password is too similar"})

@csrf_exempt
@renderer_classes((JSONRenderer))
def checkemail(request):
    email = request.POST['email']

    try:
        match = User.objects.get(email=email)
    except User.DoesNotExist:
        return JsonResponse({'Exists':False})

    return JsonResponse({'Exists':True})

@csrf_exempt
@renderer_classes((JSONRenderer))
def checkpassword(request):
    pas = request.POST['pass']

    try:
        password_validation.validate_password(pas)
        return JsonResponse({'valid':True})
    except:
        return JsonResponse({'valid':False})

######################### SSID Login ############################
@api_view(["GET","POST"])
# @permission_classes([IsAuthenticated])
def ssidpass_list(request):
    if request.method=="GET":
        device_data = ssidPassword.objects.filter(d_id=request.GET['d_id'])
        floorJson = ssidPasswordSerializers(device_data, many=True)
        # return Response(floorJson.data)
        dd = floorJson.data[:]
        return Response(dd[0])

    
    elif request.method == "POST":
        received_json_data=json.loads(request.body)
        if received_json_data['put']!='yes':
            serializer = ssidPasswordSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response("data created", status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        else:
            device_id=received_json_data['d_id']
            try:
                device123_object=ssidPassword.objects.get(d_id=device_id)
            except device123_object.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

            # del request.data['d_id']
            # print(request.data)
            serializer = ssidPasswordSerializers(device123_object, data=request.data)
            # print(serializer)
            # device_object=device.objects.filter(d_id=device_id)
            # print(device_object)
            if serializer.is_valid():
                # serializer.d_id =  device_object
                # print(serializer.d_id)
                serializer.save()
                return Response("data updated", status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET","POST"])
@permission_classes([IsAuthenticated])
def device_list(request):
    if request.method=="GET":
        device_data = device.objects.filter(user = request.user)
        floorJson = deviceSerializers(device_data, many=True)
        # return Response(floorJson.data)
        dd = floorJson.data[:]
        return Response(dd[0])

    
    elif request.method == "POST":
        received_json_data=json.loads(request.body)
        if received_json_data['put']!='yes':
            serializer = deviceSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response("data created", status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        else:
            device_id=received_json_data['d_id']
            try:
                device123_object=device.objects.get(d_id=device_id)
            except device123_object.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

            # del request.data['d_id']
            # print(request.data)
            serializer = deviceSerializers(device123_object, data=request.data)
            # print(serializer)
            # device_object=device.objects.filter(d_id=device_id)
            # print(device_object)
            if serializer.is_valid():
                # serializer.d_id =  device_object
                # print(serializer.d_id)
                serializer.save()
                return Response("data updated", status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def setup_list(request):
    if request.method=="GET":

        # data = request.data
        # user_object = User.objects.get(email=data['email'])
        floor_data = setup.objects.filter(user = request.user)
        floorJson = setuppSerializers(floor_data, many=True)
        return Response(floorJson.data)
        # dd = floorJson.data[:]
        # return Response(dd[0])

    
    elif request.method == "POST":
        received_json_data=json.loads(request.body)
        if received_json_data['put']!='yes':
            serializer = setuppSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response("data created", status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        else:
            device_id=received_json_data['d_id']
            try:
                device123_object=setup.objects.get(d_id=device_id)
            except device123_object.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

            # del request.data['d_id']
            # print(request.data)
            serializer = setuppSerializers(device123_object, data=request.data)
            # print(serializer)
            # device_object=device.objects.filter(d_id=device_id)
            # print(device_object)
            if serializer.is_valid():
                # serializer.d_id =  device_object
                # print(serializer.d_id)
                serializer.save()
                return Response("data updated", status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def setup_received(request):
    if request.method=="GET":

        # data = request.data
        # user_object = User.objects.get(email=data['email'])
        floor_data = receivedsetup.objects.filter(username=request.GET['username'])
        floorJson = recivedsetupSerializers(floor_data, many=True)
        # return Response(floorJson.data)
        # dd = floorJson.data[:]
        return Response(floorJson.data)

    
    elif request.method == "POST":
        serializer = recivedsetupSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Received to the user...!!!", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def health_list(request):
    if request.method=="GET":

        # data = request.data
        # user_object = User.objects.get(email=data['email'])
        health_data = healthrecord.objects.filter(d_id=request.GET ['d_id'])
        healthJson = recordhealthSerializers(health_data, many=True)
        # return Response(floorJson.data)
        dd = healthJson.data[:]
        return Response(dd[0])

    
    elif request.method == "POST":
        received_json_data=json.loads(request.body)
        if received_json_data['put']!='yes':
            serializer = recordhealthSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response("data created", status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        else:
            device_id=received_json_data['d_id']
            try:
                device123_object=healthrecord.objects.get(d_id=device_id)
            except device123_object.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

            # del request.data['d_id']
            # print(request.data)
            serializer = recordhealthSerializers(device123_object, data=request.data)
            # print(serializer)
            # device_object=device.objects.filter(d_id=device_id)
            # print(device_object)
            if serializer.is_valid():
                # serializer.d_id =  device_object
                # print(serializer.d_id)
                serializer.save()
                return Response("data updated", status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

                                  
@api_view(["GET","POST","PUT","DELETE"])
def profileimage(request):
    if request.method == "GET":
        device_data = userimages.objects.filter(user=request.user)
        roomJson = proimgSerializers(device_data, many=True)
        dd = roomJson.data[:]
        return Response(dd[0])

    elif request.method == "POST":
        received_json_data=json.loads(request.body)
        serializer = proimgSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("image uploded.", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "PUT":
        received_json_data=json.loads(request.body)
        device_id=received_json_data['user']
        try:
            device_object=userimages.objects.get(user=device_id)
        except device_object.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = proimgSerializers(device_object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Pic updated", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        print("exc")
        device_data = userimages.objects.filter(user = request.GET['user'])
        device_data.delete()
        return Response("Image Deleted.")



@api_view(["GET","POST","PUT","DELETE"])
def friendsuaccess(request):
    if request.method == "POST":
        # received_json_data=json.loads(request.body)
        serializer = friendaccessSerializers(data=request.data)
        if serializer.is_valid():
            print("xtz")

            serializer.save()
            # email = subuseraccess.objects.filter(user=request.GET['email'])
            # print(email)
            email12 = friendadd.objects.filter()
            subJson1 = friendaccessSerializers(email12, many=True)
            success = False
            # for x in list(subJson1.data):
            xc = list(subJson1.data)[-1]["emailtest"]
            print(xc)
                # print(email12)
                # print(subJson1.data)
            if User.objects.filter(email=xc).exists():
                # user1 = User.objects.filter(name__contains='email')
              
                success = Response("email added in friend model to use in friendlist", status=status.HTTP_201_CREATED)
            else:
                xcdelete = friendadd.objects.last()
                print(xcdelete)
                xcdelete.delete()
                return Response("Email not exists.")
            return success if success else Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # elif request.method == "DELETE":
    #     data = friendtoaccess.objects.filter(email=request.GET['email'], p_id=request.GET['p_id'])
    #     # data2 = subuseraccess.objects.filter(email=request.GET['email'])
    #     # placeJson = subuserplaceSerializers(data, many=True)
    #     data.delete()
    #     # data2.delete()
    #     return Response("removed")


@api_view(["GET","POST","PUT"])
def friendtoaddList(request):
    if request.method=="GET":
        data = friendtoaccess.objects.filter(user=request.user)
        placeJson = friendtoaccessSerializers(data, many=True)
        print(data)
        return Response(placeJson.data)
        # return Response(device_data)

    elif request.method == "POST":
        # received_json_data=json.loads(request.body)
        serializer = friendtoaccessSerializers(data=request.data)
        dd = request.data["email"]
        dd1 = request.data["user"]
        dd2 = request.data["sender_email"]
        if friendtoaccess.objects.filter(user = dd1, username = dd, sender_email = dd2).exists():
            return Response("Already sent the request")
        elif serializer.is_valid():
            serializer.save()
            email1 = friendtoaccess.objects.filter()
            subJson1 = friendtoaccessSerializers(email1, many=True)
            xc1 = list(subJson1.data)[-1]["username"]
            return Response("Sent request to: "+xc1, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "PUT":
        received_json_data=json.loads(request.body)
        device_id=received_json_data['user']
        try:
            device_object=friendtoaccess.objects.get(user=device_id)
        except device_object.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = friendtoaccessSerializers(device_object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("changed.....", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    ################ Get friend requests  ###########

@api_view(["GET","POST","PUT"])
def acceptingfriendtoaddList(request):
    if request.method=="GET":
        data = friendtoaccess.objects.filter(username=request.GET['username'])
        placeJson = friendtoaccessSerializers(data, many=True)
        print(data)
        return Response(placeJson.data)
    
    elif request.method == "PUT":
        received_json_data=json.loads(request.body)
        print(received_json_data)
        device_id=received_json_data['id']
        try:
            device_object=friendtoaccess.objects.get(id=device_id)
        except device_object.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = friendtoaccessSerializers(device_object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Successful...", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


          ########### Add Emergency Numbers   ##################



@api_view(["GET","POST","PUT"])
def emerNumber(request):
    if request.method=="GET":
        enumdata = emergencyNumber.objects.filter(user = request.user,d_id=request.GET['d_id'])
        emernumberJson = emernumberSerializers(enumdata, many=True)
        dd = emernumberJson.data[:]
        return Response(dd[0])

    elif request.method == "POST":
        received_json_data=json.loads(request.body)
        serializer = emernumberSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("data created", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method =="PUT":
        received_json_data=json.loads(request.body)
        device_id=received_json_data['d_id']
        try:
            device_object=emergencyNumber.objects.get(d_id=device_id)
        except device_object.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = emernumberSerializers(device_object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("data updated", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


           #############3 SSid Password  #################


@api_view(["GET","POST","PUT"])
def ssidList(request):
    if request.method == "GET":
        device_data = ssidPassword.objects.filter(d_id=request.GET['d_id'])
        roomJson = ssidPasswordSerializers(device_data, many=True)
        dd = roomJson.data[:]
        return Response(dd[0])

    elif request.method == "POST":
        received_json_data=json.loads(request.body)
        serializer = ssidPasswordSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("data created", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "PUT":
        received_json_data=json.loads(request.body)
        device_id=received_json_data['d_id']
        try:
            device_object=ssidPassword.objects.get(d_id=device_id)
        except device_object.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ssidPasswordSerializers(device_object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("data updated", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


            ########################  Partner Api   ###############

@api_view(["GET","POST","PUT","DELETE"])
def connectpartner(request):
    if request.method == "GET":
        device_data = partner.objects.filter(user=request.user)
        roomJson = partnersSerializers(device_data, many=True)
        dd = roomJson.data[:]
        return Response(dd[0])

    elif request.method == "POST":
        received_json_data=json.loads(request.body)
        serializer = partnersSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Partner added.Wait to confirm.", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "PUT":
        received_json_data=json.loads(request.body)
        device_id=received_json_data['user']
        try:
            device_object=partner.objects.get(user=device_id)
        except device_object.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = partnersSerializers(device_object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("partner changed.", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        print("exc")
        device_data = partner.objects.filter(user = request.GET['user'])
        device_data.delete()
        return Response("Partner Deleted.")

@api_view(["GET","POST","PUT"])
def searchrequests(request):
    if request.method == "GET":
        device_data = partner.objects.filter(email=request.GET["email"])
        roomJson = partnersSerializers(device_data, many=True)
        # dd = roomJson.data[:]
        return Response(roomJson.data)
    
    elif request.method == "PUT":
        received_json_data=json.loads(request.body)
        device_id=received_json_data['id']
        try:
            device_object=partner.objects.get(id=device_id)
        except device_object.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = partnersSerializers(device_object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Successful...", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  ############ family Api  ###########

@api_view(["GET","POST","PUT","DELETE"])
def connectmyfamily(request):
    if request.method == "GET":
        device_data = familymanaccess.objects.filter(user=request.user)
        roomJson = familyaddaccessSerializers(device_data, many=True)
        # dd = roomJson.data[:]
        # return Response(dd[0])
        return Response(roomJson.data)

    elif request.method == "POST":
        received_json_data=json.loads(request.body)
        serializer = familyaddaccessSerializers(data=request.data)
        dd = request.data["email"]
        dd1 = request.data["user"]
        print(dd)
        print(dd1)
        if familymanaccess.objects.filter(user = dd1, email = dd).exists():
            return Response("Try with another email")
        elif serializer.is_valid():
            serializer.save()
            return Response("Family member added... Wait to confirm.", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "PUT":
        received_json_data=json.loads(request.body)
        device_id=received_json_data['user']
        try:
            device_object=familymanaccess.objects.get(user=device_id)
        except device_object.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = familyaddaccessSerializers(device_object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("member changed.", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        print("exc")
        device_data = familymanaccess.objects.filter(user = request.GET['user'], email = request.GET['email'])
        device_data.delete()
        return Response("Member Deleted.")

############# SOS     ############


@api_view(["GET","POST","PUT","DELETE"])
def connectmySOS(request):
    if request.method == "GET":
        try:
            device_data = SOS.objects.filter(d_id=request.GET['d_id'])
            roomJson = allSOSSerializers(device_data, many=True)
        except Exception:
            pass

        try:
            device_data = SOS.objects.filter(user1=request.GET['user1'])
            roomJson = allSOSSerializers(device_data, many=True)
        except Exception:
            pass

        try:
            device_data = SOS.objects.filter(user2=request.GET['user2'])
            roomJson = allSOSSerializers(device_data, many=True)
        except Exception:
            pass
        
        try:
            device_data = SOS.objects.filter(user3=request.GET['user3'])
            roomJson = allSOSSerializers(device_data, many=True)
        except Exception:
            pass

        # dd = roomJson.data[:]
        # return Response(dd[0])
        return Response(roomJson.data)

    elif request.method == "POST":
        received_json_data=json.loads(request.body)
        serializer = allSOSSerializers(data=request.data)
        # dd = request.data["email"]
        # dd1 = request.data["user"]
        # print(dd)
        # print(dd1)
        # if familymanaccess.objects.filter(user = dd1, email = dd).exists():
        #     return Response("Try with another email")
        if serializer.is_valid():
            serializer.save()
            return Response("SOS added.", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "PUT":
        received_json_data=json.loads(request.body)
        device_id=received_json_data['d_id']
        try:
            device_object=SOS.objects.get(d_id=device_id)
        except device_object.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = allSOSSerializers(device_object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("SOS changed.", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        print("exc")
        device_data = SOS.objects.filter(d_id = request.GET['d_id'])
        device_data.delete()
        return Response("SOS Deleted.")

@api_view(["GET","POST","PUT"])
def searchrequestsfamily(request):
    if request.method == "GET":
        device_data = familymanaccess.objects.filter(email=request.GET["email"])
        roomJson = familyaddaccessSerializers(device_data, many=True)
        # dd = roomJson.data[:]
        return Response(roomJson.data)
    
    elif request.method == "PUT":
        received_json_data=json.loads(request.body)
        device_id=received_json_data['id']
        try:
            device_object=familymanaccess.objects.get(id=device_id)
        except device_object.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = familyaddaccessSerializers(device_object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Successful...", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def scheduleSetup(request):
    print("going")
    now = datetime.now()
    year = '{:02d}'.format(now.year)
    month = '{:02d}'.format(now.month)
    day = '{:02d}'.format(now.day)
    hour = '{:02d}'.format(now.hour)
    minute = '{:02d}'.format(now.minute)
    # second = '{:02d}'.format(now.second)
    day_month_year = '{}-{}-{}'.format(year, month, day)
    hour_minute_second = '{}:{}:00'.format(hour, minute)
    print(day_month_year)
    print(hour_minute_second)
    data1 = setup.objects.all()
    data1Json = setuppSerializers(data1, many=True)
    for data in data1Json.data:
        _date = data["date"]
        _timing = data["timing"]
        _id = data['id']
        username = data['username']
        var2 = data['email1']
        var4 = data['trigger']
        var5 = data['color']
        var6 = data['ring']
        var7 = data['long_tude']
        var71 = data['lat_tude']
        var8 = data['song']
        var9 = data['emoji']
        var10 = data['message']
        print(username)

    # dataJson = pinscheduleTimeSerializers(data1, many=True)
        if _date<=day_month_year and _timing<=hour_minute_second:
            print("nono1")
            # if setup.objects.filter(id=_id):
            #     print("nono2")
            if (username != None):
                print("nono3")
                BASE_URL = f'https://pendant.herokuapp.com/receivethesetup/'#'https://genorion1.herokuapp.com/getpostdevicePinStatus/?d_id=DIDM12932021AAAAAA'
                print("xxxxxxx1")
                token = "761a98f16bd3919ddd717cf3c2f8c05aa2ed2a18"

                headers =  {'content-type' : 'application/json',
                            'Authorization': "Token {}".format(token)}
                data = {'username':username,
                'email':var2,
                'trigger':var4,
                'color':var5,
                'ring':var6,
                'long_tude':var7,
                'lat_tude':var71,
                 'song':var8,
                 'emoji':var9,
                 'message':var10}
                print("xxx1")
                auth_response = requests.post(BASE_URL, headers=headers, data=json.dumps(data))
                auth_response.text
                print(auth_response)
                data2 = setup.objects.filter(id=_id)
                print("matched")
                data2.delete()
                print("deleted")
        else:
            print("its ok try again..!!")
    return render(request, 'setup.html')


########################### login / register  ##########

def userlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username= username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('change_password/')
        else:
            messages.info(request,'invalid')
            return redirect('/userlogin')
    else:
        return render(request, 'userlogin.html')


        ################### reset password   ################



                       ################### Change Password #####################


@login_required(login_url="/userlogin")
def change_pass(request):
    if request.method == "POST":
        frm = PasswordChangeForm(user=request.user, data=request.POST)
        if frm.is_valid():
            frm.save()
            return HttpResponse('Password Changed, Now go to the app and LOGIN with your new Password.')
    else:
        frm = PasswordChangeForm(user=request.user)
    return render(request, 'change_password.html', {'form': frm})

# @login_required(login_url="/flutter_change_password_login")
# def change_passwo(request):
#     if request.method == "POST":
#         frm = PasswordChangeForm(user=request.user, data=request.POST)
#         if frm.is_valid():
#             frm.save()
#             return HttpResponse("Password Changed")
#     else:
#         frm = PasswordChangeForm(user=request.user)
#     return render(request, 'change_password_flu.html', {'form': frm})

# def flutter_change_password_login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = auth.authenticate(username= username,password=password)

#         if user is not None:
#             auth.login(request, user)
#             return redirect('/change_password_flu')
#         else:
#             messages.info(request,'invalid')
#             return redirect('flutter_change_password_login')
#     else:
#         return render(request, 'flutter_change_password_login.html')