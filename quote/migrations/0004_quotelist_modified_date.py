# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-17 14:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0003_auto_20180515_2009'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotelist',
            name='modified_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
