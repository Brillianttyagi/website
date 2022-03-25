# Generated by Django 3.0.8 on 2021-03-06 13:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventory',
            old_name='description',
            new_name='Description',
        ),
        migrations.RenameField(
            model_name='inventory',
            old_name='guarantee',
            new_name='Guarantee',
        ),
        migrations.RenameField(
            model_name='inventory',
            old_name='hsnCode',
            new_name='HSN',
        ),
        migrations.RenameField(
            model_name='inventory',
            old_name='warranty',
            new_name='Warranty',
        ),
        migrations.RenameField(
            model_name='inventory',
            old_name='colour',
            new_name='colors',
        ),
        migrations.RenameField(
            model_name='inventory',
            old_name='country',
            new_name='countryoforigin',
        ),
        migrations.RenameField(
            model_name='inventory',
            old_name='status',
            new_name='inventorystatus',
        ),
        migrations.RenameField(
            model_name='inventory',
            old_name='Tittle',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='inventory',
            old_name='sellPrice',
            new_name='sellingPrice',
        ),
        migrations.RenameField(
            model_name='inventory',
            old_name='subCategory',
            new_name='sub_Category',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='basePrice',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='city',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='date',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='product_deatails',
        ),
        migrations.AddField(
            model_name='inventory',
            name='listedPrice',
            field=models.FloatField(default=34, validators=[django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inventory',
            name='pricedetails',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='inventory',
            name='productparameters',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='inventory',
            name='productweight',
            field=models.PositiveIntegerField(default=34),
            preserve_default=False,
        ),
    ]
