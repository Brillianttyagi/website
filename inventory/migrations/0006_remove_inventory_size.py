# Generated by Django 3.0.8 on 2021-03-06 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_inventory_shippingwithseventhsquare'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory',
            name='size',
        ),
    ]
