# Generated by Django 2.0 on 2017-12-26 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=300, unique=True)),
                ('token', models.CharField(max_length=1000, unique=True)),
                ('uclapi_token', models.CharField(max_length=1000, unique=True)),
            ],
        ),
    ]
