# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-19 14:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0004_quotelist_modified_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quotelist',
            name='modified_date',
        ),
    ]
