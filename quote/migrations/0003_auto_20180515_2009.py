# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-15 11:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0002_quotelist_added_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotelist',
            name='name',
            field=models.CharField(default='관리자', max_length=50),
        ),
        migrations.AddField(
            model_name='quotelist',
            name='original',
            field=models.CharField(default='Out of this World', max_length=150),
        ),
        migrations.AddField(
            model_name='quotelist',
            name='translated',
            field=models.CharField(default='이승탈출', max_length=150),
        ),
    ]
