# Generated by Django 3.1.2 on 2021-08-05 16:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0014_auto_20210706_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='sellingPrice',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
