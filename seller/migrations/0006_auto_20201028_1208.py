# Generated by Django 3.1.2 on 2020-10-28 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0005_auto_20201027_0014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notify',
            name='n4',
        ),
        migrations.RemoveField(
            model_name='notify',
            name='n5',
        ),
        migrations.RemoveField(
            model_name='notify',
            name='s4',
        ),
        migrations.RemoveField(
            model_name='notify',
            name='s5',
        ),
        migrations.AddField(
            model_name='notify',
            name='coun',
            field=models.IntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='notify',
            name='notifications',
            field=models.CharField(max_length=15, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='s_prod',
            name='listed',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='s_prod',
            name='marked',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='s_prod',
            name='prod_h',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='s_prod',
            name='prod_l',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='s_prod',
            name='prod_w',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]