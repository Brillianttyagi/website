# Generated by Django 3.0.8 on 2021-02-23 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]