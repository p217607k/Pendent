from typing import AbstractSet
from django.contrib import messages
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
        return self.d_name


class emergencyNumber(models.Model):
    d_id = models.OneToOneField(allDevices, on_delete=models.CASCADE)
    number1 = models.BigIntegerField(blank=True, null=True)
    number2 = models.BigIntegerField(blank=True, null=True)
    number3 = models.BigIntegerField(blank=True, null=True)


class setup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email1 = models.CharField(max_length=50, blank=False)
    username = models.ForeignKey(allusernames, on_delete=models.CASCADE)
    # email = models.ForeignKey(allEmail, on_delete=models.CASCADE)
    date = models.DateField(default="2000-01-01", null=True)
    timing = models.TimeField(default='00:00')
    trigger = models.CharField(max_length=20, blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    ring = models.IntegerField(blank=True, null=True)
    long_tude = models.DecimalField(max_digits=30, decimal_places=10, blank=True, null=True)
    lat_tude = models.DecimalField(max_digits=30, decimal_places=10, blank=True, null=True)
    song = models.IntegerField(default=0, blank=True, null=True)
    emoji = models.IntegerField(default=0, blank=True, null=True)
    message = models.TextField(max_length=999, blank=True, null=True)

    def __str__(self):
        return self.email1

class receivedsetup(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50, blank=True, null=True)
    trigger = models.CharField(max_length=20, blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    ring = models.IntegerField(blank=True, null=True)
    long_tude = models.DecimalField(max_digits=30, decimal_places=10, blank=True, null=True)
    lat_tude = models.DecimalField(max_digits=30, decimal_places=10, blank=True, null=True)
    song = models.IntegerField(default=0, blank=True, null=True)
    emoji = models.IntegerField(default=0, blank=True, null=True)
    message = models.TextField(max_length=999, blank=True, null=True)

    def __str__(self):
        return self.username


class userimages(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    file = models.CharField(max_length=499999, blank=True, default=defprofoto())


class friendadd(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    emailtest = EmailField()
    email = models.CharField(primary_key=True, max_length=100)

    def __str__(self):
        return self.email


class friendtoaccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sender_email = models.CharField(max_length=50, blank=False)
    sender_username = models.CharField(max_length=50, blank=True, null=True) #sender username
    first_name = models.CharField(max_length=50, blank=True, null=True) #sender name
    username = models.ForeignKey(allusernames, on_delete=models.CASCADE)
    trigger = models.IntegerField(default=0)

    def __str__(self):
        return self.sender_email

class familymanaccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sender_email = models.CharField(max_length=50, blank=False)  # sender email
    d_id_sender = models.ForeignKey(allDevices, on_delete=models.CASCADE, default=0) # sender device_id
    sender_username = models.CharField(max_length=50, blank=True, null=True) #sender username
    first_name = models.CharField(max_length=50, blank=True, null=True) #sender name
    username = models.ForeignKey(allusernames, on_delete=models.CASCADE)
    d_id_receiver = models.CharField(max_length=50, blank=True, null=True) # reciever device_id
    trigger = models.IntegerField(default=0)

    def __str__(self):
        return self.sender_email

class SOS(models.Model):
    d_id = models.OneToOneField(allDevices, on_delete=models.CASCADE)
    long_tude = models.DecimalField(max_digits=30, decimal_places=10, blank=True, null=True)
    lat_tude = models.DecimalField(max_digits=30, decimal_places=10, blank=True, null=True)
    message = models.CharField(max_length=99, blank=True, null=True)
    ring = models.IntegerField(blank=True, null=True)
    user1 = models.CharField(max_length=50, blank=True, null=True)
    user2 = models.CharField(max_length=50, blank=True, null=True)
    user3 = models.CharField(max_length=50, blank=True, null=True)


class partner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sender_email = models.CharField(max_length=50, blank=False) #send by this
    d_id_sender = models.ForeignKey(allDevices, on_delete=models.CASCADE, default=0) # sender device_id
    sender_username = models.CharField(max_length=50, blank=True, null=True) #sender username
    first_name = models.CharField(max_length=50, blank=True, null=True) #sender name
    username = models.ForeignKey(allusernames, on_delete=models.CASCADE) #sending to this username
    d_id_receiver = models.CharField(max_length=50, blank=True, null=True) # receiver device_id
    trigger = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.sender_email


class healthrecord(models.Model):
    d_id = models.OneToOneField(allDevices, on_delete=models.CASCADE)
    # deviceName=models.CharField(max_length=40)
    healthS1 = models.FloatField(blank=True, null=True)
    healthS2 = models.FloatField(blank=True, null=True)
    healthS3 = models.FloatField(blank=True, null=True)
    healthS4 = models.FloatField(blank=True, null=True)


class ssidPassword(models.Model):
    d_id = models.OneToOneField(allDevices, on_delete=models.CASCADE)
    ssid1 = models.CharField(unique=True, max_length=15)
    password1 = models.CharField(null=False, max_length=50)
    ssid2 = models.CharField(unique=True, max_length=15)
    password2 = models.CharField(null=False, max_length=50)
    ssid3 = models.CharField(unique=True, max_length=15)
    password3 = models.CharField(null=False, max_length=50)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
