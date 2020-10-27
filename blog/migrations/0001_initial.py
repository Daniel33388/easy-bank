# Generated by Django 3.0.8 on 2020-10-23 17:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('author', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('article', models.TextField()),
                ('date', models.DateField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
