# Generated by Django 3.1.2 on 2021-06-30 21:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_auto_20210701_0234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='mobileNumber',
            field=models.TextField(max_length=13, validators=[django.core.validators.RegexValidator(message='Invalid mobile number', regex='^[6-9]\\d{9}$')]),
        ),
    ]