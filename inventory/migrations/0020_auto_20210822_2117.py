# Generated by Django 3.1.2 on 2021-08-22 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0019_auto_20210821_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]