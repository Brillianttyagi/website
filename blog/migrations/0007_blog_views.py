# Generated by Django 2.2.13 on 2021-08-04 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210802_2150'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
