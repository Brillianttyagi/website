# Generated by Django 3.0.8 on 2021-02-23 19:46

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accountHolderName', models.CharField(max_length=30)),
                ('accontNumber', models.CharField(max_length=30, unique=True)),
                ('ifsc', models.CharField(max_length=30)),
                ('bank', models.CharField(max_length=30)),
                ('branch', models.CharField(max_length=30)),
                ('status', models.CharField(choices=[('YES', 'Yes'), ('NO', 'No'), ('Invalid', 'Invalid')], default='NO', max_length=10)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]