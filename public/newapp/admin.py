from django.contrib import admin
from . models import *
# Register your models here.


admin.site.register(setup)
admin.site.register(device)
admin.site.register(healthrecord)
admin.site.register(ssidPassword)
# admin.site.register(sendRecivedMeassages)