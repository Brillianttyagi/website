# Generated by Django 3.1.2 on 2021-08-23 17:50

import account.models
import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_auto_20210822_2117'),
    ]

    operations = [
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
    ]
