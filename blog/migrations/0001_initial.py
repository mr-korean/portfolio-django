# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-05 09:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='TITLE')),
                ('slug', models.SlugField(allow_unicode=True, help_text='제목 대신 쓰이는 한 단어.', unique=True, verbose_name='SLUG')),
                ('description', models.CharField(blank=True, help_text='간단한 설명.', max_length=100, verbose_name='DESCRIPTION')),
                ('content', models.TextField(verbose_name='CONTENT')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('modify_date', models.DateTimeField(auto_now=True, verbose_name='Modified Date')),
            ],
            options={
                'verbose_name': 'note',
                'verbose_name_plural': 'notes',
                'db_table': 'blog_note',
                'ordering': ('-modify_date',),
            },
        ),
    ]