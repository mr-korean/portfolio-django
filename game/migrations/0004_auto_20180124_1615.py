# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-24 07:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_auto_20180123_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='highscore',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='record',
            name='level',
            field=models.TextField(default='1'),
        ),
        migrations.AlterField(
            model_name='record',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
