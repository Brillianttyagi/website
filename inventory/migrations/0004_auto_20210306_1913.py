# Generated by Django 3.0.8 on 2021-03-06 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20210306_1853'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventory',
            old_name='listedPrice',
            new_name='markedPrice',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='pricedetails',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='productparameters',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='productweight',
        ),
    ]
