# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-19 09:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0007_auto_20180702_0448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotelist',
            name='name',
            field=models.CharField(default='관리자', max_length=50),
        ),
        migrations.AlterField(
            model_name='quotelist',
            name='translated',
            field=models.CharField(default='이승탈출', max_length=150),
        ),
    ]