# Generated by Django 3.1.2 on 2021-08-02 10:43

import account.models
import django.core.files.storage
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_auto_20210701_0250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='GSTDoc',
            field=models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='F:\\Seventh Square Work\\seller.seventhsq.com\\KYCDoc'), upload_to=account.models.get_file_path_company_gst_doc),
        ),
        migrations.AlterField(
            model_name='account',
            name='RepresentativeDoc',
            field=models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='F:\\Seventh Square Work\\seller.seventhsq.com\\KYCDoc'), upload_to=account.models.get_file_path_company_repr_doc),
        ),
        migrations.AlterField(
            model_name='account',
            name='companyKYCDOC',
            field=models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='F:\\Seventh Square Work\\seller.seventhsq.com\\KYCDoc'), upload_to=account.models.get_file_path_company_doc),
        ),
        migrations.AlterField(
            model_name='account',
            name='mobileNumber',
            field=models.CharField(max_length=13, unique=True, validators=[django.core.validators.RegexValidator(message='Invalid mobile number', regex='^[6-9]\\d{9}$')]),
        ),
    ]