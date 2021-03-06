# Generated by Django 3.1.2 on 2020-10-21 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0002_auto_20201021_0033'),
    ]

    operations = [
        migrations.AddField(
            model_name='s_prod',
            name='frstimg',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='s_prod',
            name='box_h',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='s_prod',
            name='box_l',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='s_prod',
            name='box_w',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='s_prod',
            name='disbursement',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='s_prod',
            name='listed',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='s_prod',
            name='marked',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='s_prod',
            name='prod_h',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='s_prod',
            name='prod_l',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='s_prod',
            name='prod_w',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='s_prod',
            name='s_weight',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='s_prod',
            name='sale',
            field=models.FloatField(default=0),
        ),
    ]
