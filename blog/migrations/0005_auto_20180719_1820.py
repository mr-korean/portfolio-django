# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-19 09:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180702_0448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='content',
            field=models.TextField(verbose_name='내용'),
        ),
        migrations.AlterField(
            model_name='note',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='생성일'),
        ),
        migrations.AlterField(
            model_name='note',
            name='description',
            field=models.CharField(blank=True, help_text='간단한 설명.', max_length=100, verbose_name='설명'),
        ),
        migrations.AlterField(
            model_name='note',
            name='modify_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='수정일'),
        ),
        migrations.AlterField(
            model_name='note',
            name='slug',
            field=models.SlugField(allow_unicode=True, help_text='제목 대신 쓰이는 한 단어.', unique=True, verbose_name='키워드'),
        ),
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.CharField(max_length=50, verbose_name='제목'),
        ),
    ]
