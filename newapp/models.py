from typing import AbstractSet
from django.db import models
from django.conf import Settings, settings
from django.db.models.signals import post_save
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AbstractUser, User
from django.db.models.fields import CharField, EmailField
from newapp.utils import defprofoto


# class User(AbstractUser):
#     pass


class allDevices(models.Model):
    d_id = models.CharField(max_length=40, default=0, primary_key=True)

    def __str__(self):
        return self.d_id


class allEmail(models.Model):
    email = models.CharField(max_length=50 ,primary_key=True)

    def __str__(self):
        return self.email

class allusernames(models.Model):
    username = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.username


class device(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    d_id = models.OneToOneField(allDevices, on_delete=models.CASCADE)
    d_name = models.CharField(max_length=15)

    def __str__(self):
        return self.d_id


class emergencyNumber(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    d_id = models.OneToOneField(allDevices, on_delete=models.CASCADE)
    number1 = models.BigIntegerField(blank=True, null=True)
    number2 = models.BigIntegerField(blank=True, null=True)
    number3 = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return self.d_id

class setup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email1 = models.CharField(max_length=50, blank=False)
    username = models.ForeignKey(allusernames, on_delete=models.CASCADE)
    # email = models.ForeignKey(allEmail, on_delete=models.CASCADE)
    date = models.DateField(default="2000-01-01", null=True)
    timing = models.TimeField(default='00:00')
    s_id = models.CharField(unique=True, max_length=20)
    trigger = models.CharField(unique=True, max_length=20, null=True)
    color = models.CharField(max_length=50, null=True)
    ring = models.IntegerField(null=True)
    location = models.CharField(null=True, max_length=199)
    song = models.IntegerField(default=0, null=True)
    emoji = models.IntegerField(default=0, null=True)
    message = models.TextField(max_length=999, blank=True)

    def __str__(self):
        return self.user

class receivedsetup(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50, blank=False)
    s_id = models.CharField(unique=True, max_length=20)
    trigger = models.CharField(unique=True, max_length=20, null=True)
    color = models.CharField(max_length=50, null=True)
    ring = models.IntegerField(null=True)
    location = models.CharField(null=True, max_length=199)
    song = models.IntegerField(default=0, null=True)
    emoji = models.IntegerField(default=0, null=True)
    message = models.TextField(max_length=999, blank=True)

    def __str__(self):
        return self.username


class userimages(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    file = models.CharField(max_length=499999, blank=True, default=defprofoto())

    def __str__(self):
        return self.user


class friendadd(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    emailtest = EmailField()
    email = models.CharField(primary_key=True, max_length=100)

    def __str__(self):
        return self.email


class friendtoaccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email1 = models.CharField(max_length=50, blank=False)
    email = models.ForeignKey(friendadd, on_delete=models.CASCADE)
    trigger = models.IntegerField(default=0)

    def __str__(self):
        return self.user

class familymanaccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email1 = models.CharField(max_length=50, blank=False)
    email = models.ForeignKey(allEmail, on_delete=models.CASCADE)
    d_id = models.ForeignKey(allDevices, on_delete=models.CASCADE, default=0)
    trigger = models.IntegerField(default=0)

    def __str__(self):
        return self.user


class partner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email1 = models.CharField(max_length=50, blank=False) #send by this
    email = models.ForeignKey(allEmail, on_delete=models.CASCADE) #sending to this email
    trigger = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.user


class healthrecord(models.Model):
    d_id = models.OneToOneField(allDevices, on_delete=models.CASCADE)
    # deviceName=models.CharField(max_length=40)
    healthS1 = models.FloatField(blank=True, null=True)
    healthS2 = models.FloatField(blank=True, null=True)
    healthS3 = models.FloatField(blank=True, null=True)
    healthS4 = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.d_id


class ssidPassword(models.Model):
    d_id = models.OneToOneField(allDevices, on_delete=models.CASCADE)
    ssid1 = models.CharField(unique=True, max_length=15)
    password1 = models.CharField(null=False, max_length=50)
    ssid2 = models.CharField(unique=True, max_length=15)
    password2 = models.CharField(null=False, max_length=50)
    ssid3 = models.CharField(unique=True, max_length=15)
    password3 = models.CharField(null=False, max_length=50)

    def __str__(self):
        return self.d_id

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
