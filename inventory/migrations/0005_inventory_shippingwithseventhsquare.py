# Generated by Django 3.0.8 on 2021-03-06 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_auto_20210306_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='shippingWithSeventhSquare',
            field=models.BooleanField(default=True),
        ),
    ]