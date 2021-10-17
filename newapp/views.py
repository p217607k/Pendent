from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth.models import User
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
from rest_framework.permissions import IsAuthenticated
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
# import pyrebase

# config={
#     "apiKey": "AIzaSyBlKT-0XpVHAP-YqpAgEH93fmN6AyIds_s",
#     "authDomain": "genorion-79a43.firebaseapp.com",
#     "databaseURL": "https://genorion-79a43-default-rtdb.firebaseio.com/",
#     "projectId": "genorion-79a43",
#     "storageBucket": "genorion-79a43.appspot.com",
#     "messagingSenderId": "109228463289",
#     "appId": "1:109228463289:web:45b5d3e15401c007483768",
#     "measurementId": "G-WM79VJNKRH"
# }
# firebase = pyrebase.initialize_app(config)
# auth = firebase.auth()
# database = firebase.database()


conn = http.client.HTTPConnection("2factor.in")

@api_view(["GET"])
# @permission_classes([IsAuthenticated])
def useridList(request):
    if request.method=="GET":
        current_user = request.user
        print(current_user.id)
        return Response(current_user.id)

# Create your views here.

def index(request):
    return render(request, 'index.html')


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
        d = allEmail.objects.create(email = e)
        d.save()
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
        floor_data = setup.objects.filter(user = request.user,d_id=request.GET ['d_id'])
        floorJson = setupSerializers(floor_data, many=True)
        # return Response(floorJson.data)
        dd = floorJson.data[:]
        return Response(dd[0])

    
    elif request.method == "POST":
        received_json_data=json.loads(request.body)
        if received_json_data['put']!='yes':
            serializer = setupSerializers(data=request.data)
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
            serializer = setupSerializers(device123_object, data=request.data)
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
        if serializer.is_valid():
            serializer.save()
            email1 = friendtoaccess.objects.filter()
            subJson1 = friendtoaccessSerializers(email1, many=True)
            xc1 = list(subJson1.data)[-1]["email"]
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
        data = friendtoaccess.objects.filter(email=request.GET['email'])
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
