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