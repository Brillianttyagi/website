# Generated by Django 3.1.2 on 2020-10-20 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='s_prod',
            name='prod_1img',
        ),
        migrations.AddField(
            model_name='new_sup',
            name='c_represent',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='new_sup',
            name='categories',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='new_sup',
            name='id_verified',
            field=models.CharField(default='No', max_length=10),
        ),
        migrations.AddField(
            model_name='s_prod',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='new_sup',
            name='verified',
            field=models.CharField(default='No', max_length=10),
        ),
    ]
