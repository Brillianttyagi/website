# Generated by Django 2.2.19 on 2021-05-25 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0004_auto_20210226_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='bank',
            name='mobile',
            field=models.CharField(default='', max_length=13),
        ),
    ]
