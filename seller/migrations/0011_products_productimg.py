# Generated by Django 3.1.2 on 2020-11-02 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0010_auto_20201030_2313'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='productimg',
            field=models.IntegerField(default=1),
        ),
    ]
