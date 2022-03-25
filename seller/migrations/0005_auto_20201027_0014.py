# Generated by Django 3.1.2 on 2020-10-26 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0004_new_sup_comm'),
    ]

    operations = [
        migrations.AddField(
            model_name='new_sup',
            name='account_status',
            field=models.CharField(default='Active', max_length=10),
        ),
        migrations.AddField(
            model_name='new_sup',
            name='bank_verified',
            field=models.CharField(default='No', max_length=4),
        ),
        migrations.AddField(
            model_name='s_prod',
            name='guarantee',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='s_prod',
            name='prod_status',
            field=models.CharField(default='Inactive', max_length=10),
        ),
        migrations.AddField(
            model_name='s_prod',
            name='warranty',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='new_sup',
            name='id_verified',
            field=models.CharField(default='No', max_length=4),
        ),
        migrations.AlterField(
            model_name='new_sup',
            name='verified',
            field=models.CharField(default='No', max_length=4),
        ),
        migrations.CreateModel(
            name='Notify',
            fields=[
                ('notifications', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('n1', models.CharField(blank=True, max_length=100, null=True)),
                ('s1', models.IntegerField(default=800)),
                ('n2', models.CharField(blank=True, max_length=100, null=True)),
                ('s2', models.IntegerField(default=800)),
                ('n3', models.CharField(blank=True, max_length=100, null=True)),
                ('s3', models.IntegerField(default=800)),
                ('n4', models.CharField(blank=True, max_length=100, null=True)),
                ('s4', models.IntegerField(default=800)),
                ('n5', models.CharField(blank=True, max_length=100, null=True)),
                ('s5', models.IntegerField(default=800)),
                ('sup_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='seller.new_sup')),
            ],
        ),
    ]