# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-05 09:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_auto_20171203_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created Date'),
        ),
        migrations.AlterField(
            model_name='post',
            name='modify_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Modified Date'),
        ),
    ]
