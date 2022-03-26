# Generated by Django 3.1.2 on 2021-08-24 13:47

import account.models
import django.core.files.storage
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0017_merge_20210824_1914'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='gstin_data',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='gstin_data_status',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='GSTDoc',
            field=models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='/home/seventh/seventhsqctest/KYCDoc'), upload_to=account.models.get_file_path_company_gst_doc),
        ),
        migrations.AlterField(
            model_name='account',
            name='RepresentativeDoc',
            field=models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='/home/seventh/seventhsqctest/KYCDoc'), upload_to=account.models.get_file_path_company_repr_doc),
        ),
        migrations.AlterField(
            model_name='account',
            name='companyKYCDOC',
            field=models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='/home/seventh/seventhsqctest/KYCDoc'), upload_to=account.models.get_file_path_company_doc),
        ),
        migrations.AlterField(
            model_name='account',
            name='mobileNumber',
            field=models.TextField(max_length=13, unique=True, validators=[django.core.validators.RegexValidator(message='Invalid mobile number', regex='^[6-9]\\d{9}$')]),
        ),
    ]
