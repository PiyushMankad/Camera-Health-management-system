# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-12 07:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cameradb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EntryID', models.CharField(max_length=30)),
                ('InfoCode', models.CharField(max_length=30)),
                ('InfoType', models.CharField(max_length=50)),
                ('TimeStamp', models.DateField()),
                ('CameraID', models.CharField(max_length=20)),
                ('CameraStatus', models.CharField(max_length=50)),
                ('Action', models.CharField(max_length=20)),
            ],
        ),
    ]