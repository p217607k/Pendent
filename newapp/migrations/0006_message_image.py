# Generated by Django 4.1.5 on 2023-04-23 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0005_alter_device_id_alter_emergencynumber_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='image',
            field=models.ImageField(default='', upload_to='ws/image'),
            preserve_default=False,
        ),
    ]