# Generated by Django 3.1.1 on 2021-11-05 09:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='allDevices',
            fields=[
                ('d_id', models.CharField(default=0, max_length=40, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='allEmail',
            fields=[
                ('email', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='allusernames',
            fields=[
                ('username', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='friendadd',
            fields=[
                ('emailtest', models.EmailField(max_length=254)),
                ('email', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='receivedsetup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('trigger', models.CharField(blank=True, max_length=20, null=True)),
                ('color', models.CharField(blank=True, max_length=50, null=True)),
                ('ring', models.IntegerField(blank=True, null=True)),
                ('long_tude', models.DecimalField(decimal_places=10, max_digits=30)),
                ('lat_tude', models.DecimalField(decimal_places=10, max_digits=30)),
                ('song', models.IntegerField(blank=True, default=0, null=True)),
                ('emoji', models.IntegerField(blank=True, default=0, null=True)),
                ('message', models.TextField(blank=True, max_length=999, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='userimages',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('file', models.CharField(blank=True, default='', max_length=499999)),
            ],
        ),
        migrations.CreateModel(
            name='ssidPassword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ssid1', models.CharField(max_length=15, unique=True)),
                ('password1', models.CharField(max_length=50)),
                ('ssid2', models.CharField(max_length=15, unique=True)),
                ('password2', models.CharField(max_length=50)),
                ('ssid3', models.CharField(max_length=15, unique=True)),
                ('password3', models.CharField(max_length=50)),
                ('d_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='newapp.alldevices')),
            ],
        ),
        migrations.CreateModel(
            name='SOS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long_tude', models.DecimalField(decimal_places=10, max_digits=30)),
                ('lat_tude', models.DecimalField(decimal_places=10, max_digits=30)),
                ('message', models.CharField(blank=True, max_length=99, null=True)),
                ('ring', models.IntegerField(blank=True, null=True)),
                ('user1', models.CharField(blank=True, max_length=50, null=True)),
                ('user2', models.CharField(blank=True, max_length=50, null=True)),
                ('user3', models.CharField(blank=True, max_length=50, null=True)),
                ('d_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='newapp.alldevices')),
            ],
        ),
        migrations.CreateModel(
            name='setup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email1', models.CharField(max_length=50)),
                ('date', models.DateField(default='2000-01-01', null=True)),
                ('timing', models.TimeField(default='00:00')),
                ('trigger', models.CharField(blank=True, max_length=20, null=True)),
                ('color', models.CharField(blank=True, max_length=50, null=True)),
                ('ring', models.IntegerField(blank=True, null=True)),
                ('long_tude', models.DecimalField(decimal_places=10, max_digits=30)),
                ('lat_tude', models.DecimalField(decimal_places=10, max_digits=30)),
                ('song', models.IntegerField(blank=True, default=0, null=True)),
                ('emoji', models.IntegerField(blank=True, default=0, null=True)),
                ('message', models.TextField(blank=True, max_length=999, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newapp.allusernames')),
            ],
        ),
        migrations.CreateModel(
            name='partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_email', models.CharField(max_length=50)),
                ('username', models.CharField(blank=True, max_length=50, null=True)),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('d_id_receiver', models.CharField(blank=True, max_length=50, null=True)),
                ('trigger', models.IntegerField(default=0)),
                ('d_id_sender', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='newapp.alldevices')),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newapp.allemail')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='healthrecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('healthS1', models.FloatField(blank=True, null=True)),
                ('healthS2', models.FloatField(blank=True, null=True)),
                ('healthS3', models.FloatField(blank=True, null=True)),
                ('healthS4', models.FloatField(blank=True, null=True)),
                ('d_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='newapp.alldevices')),
            ],
        ),
        migrations.CreateModel(
            name='friendtoaccess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_email', models.CharField(max_length=50)),
                ('username', models.CharField(blank=True, max_length=50, null=True)),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('trigger', models.IntegerField(default=0)),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newapp.friendadd')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='familymanaccess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_email', models.CharField(max_length=50)),
                ('username', models.CharField(blank=True, max_length=50, null=True)),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('d_id_receiver', models.CharField(blank=True, max_length=50, null=True)),
                ('trigger', models.IntegerField(default=0)),
                ('d_id_sender', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='newapp.alldevices')),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newapp.allemail')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='emergencyNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number1', models.BigIntegerField(blank=True, null=True)),
                ('number2', models.BigIntegerField(blank=True, null=True)),
                ('number3', models.BigIntegerField(blank=True, null=True)),
                ('d_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='newapp.alldevices')),
            ],
        ),
        migrations.CreateModel(
            name='device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_name', models.CharField(max_length=15)),
                ('d_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='newapp.alldevices')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
