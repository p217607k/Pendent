from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

# Create your models here.

class device(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    d_id = models.CharField(unique=True, max_length=20)
    d_name = models.CharField(max_length=15)

class setup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    d_id = models.ForeignKey(device, on_delete=models.CASCADE)
    s_id = models.CharField(unique = True, max_length=20)
    trigger = models.CharField(unique=True, max_length=20)
    color = models.CharField(max_length=15)
    ring = models.IntegerField(null=False)
    message = models.TextField(max_length=999)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)