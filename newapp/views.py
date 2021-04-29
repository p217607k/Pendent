from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from .forms import UserRegisterForm
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from newapp.serializers import deviceSerializers, setupSerializers, recordhealthSerializers, ssidPasswordSerializers
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


conn = http.client.HTTPConnection("2factor.in")



# Create your views here.

def index(request):
    return render(request, 'index.html')


@csrf_exempt
@renderer_classes((JSONRenderer))
def register_flutter(request):
    form = UserRegisterForm(request.POST)
    # print(request.POST)
    # print(form)
    if form.is_valid():
        form.save()
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
        device_data = device.objects.filter(user = request.user,d_id=request.GET['d_id'])
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