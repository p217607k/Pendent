from django.contrib import admin
from . models import *
# Register your models here.

admin.site.register(Message)

admin.site.register(setup)
admin.site.register(device)
admin.site.register(healthrecord)
admin.site.register(ssidPassword)
admin.site.register(emergencyNumber)
admin.site.register(userimages)
admin.site.register(allEmail)
admin.site.register(allusernames)
admin.site.register(friendadd)
admin.site.register(friendtoaccess)
admin.site.register(partner)
admin.site.register(allDevices)
admin.site.register(receivedsetup)
admin.site.register(familymanaccess)
admin.site.register(SOS)

# admin.site.register(sendRecivedMeassages)

# class FriendListAdmin(admin.ModelAdmin):
#     list_filter = ['user']
#     list_display = ['user']
#     search_fields = ['user']
#     readonly_fields = ['user']

#     class Meta:
#         model = FriendList

# admin.site.register(FriendList, FriendListAdmin)

# class FriendRequestAdmin(admin.ModelAdmin):
#     list_filter = ['sender', 'receiver']
#     list_display = ['sender', 'receiver']
#     search_fields = ['sender__username', 'receiver__username']

#     class Meta:
#         model = FriendRequest

# admin.site.register(FriendRequest, FriendRequestAdmin)
    