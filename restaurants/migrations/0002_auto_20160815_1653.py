# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-15 16:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='disliked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='review',
            name='team',
            field=models.CharField(default='Team Valor', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='review',
            name='comment',
            field=models.TextField(unique=True),
        ),
    ]
