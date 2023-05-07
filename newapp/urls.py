from django.urls import path,include
from django.conf import settings
from newapp import views
# from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

app_name = 'newapp'


urlpatterns = [

    path('', views.index, name='homepage'),
    path('<str:room_name>/', views.room, name='room'),
    # path('<str:room_name>/', views.room, name='room'),
    path('registertodent/',views.register_flutter,name='flutter-register'),
    path('ckeckingmail/',views.checkemail,name='email-check'),
    path('ckeckingpassword/',views.checkpassword,name='pass-check'),
    path('userlogin/', views.userlogin, name='userlogin'),
    
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="password_reset.html"), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), name='password_reset_complete'),
    path('change_password/', views.change_pass, name='change_password'),
    # path('change_password_phone/', views.change_passwo, name='change_password'),
    # path('flutter_change_password_login', views.flutter_change_password_login, name='flutter_change_password_login'),
    # path('change_password_flu/', views.change_pass, name='change_password'),
    
]