# Generated by Django 3.0.8 on 2021-03-06 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_remove_inventory_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='inventoryStatus',
            field=models.BooleanField(default=True),
        ),
    ]
