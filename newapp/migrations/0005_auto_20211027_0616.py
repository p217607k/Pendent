# Generated by Django 3.1.1 on 2021-10-27 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0004_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allemail',
            name='email',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='allusernames',
            name='username',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
