# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-13 20:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0003_auto_20160813_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='username',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
