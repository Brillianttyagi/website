# Generated by Django 2.2.13 on 2021-08-02 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField(max_length=100000)),
                ('created', models.DateField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='pics')),
                ('author', models.CharField(max_length=60)),
                ('tags', models.TextField(max_length=100000)),
            ],
        ),
    ]
