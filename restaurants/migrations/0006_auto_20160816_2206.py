# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-16 22:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0005_auto_20160815_2359'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visit',
            name='restaurant',
        ),
        migrations.RemoveField(
            model_name='visit',
            name='team',
        ),
        migrations.DeleteModel(
            name='Visit',
        ),
    ]