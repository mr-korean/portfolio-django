# -*- coding: UTF-8 -*-

from django.db import models
from django.utils import timezone
from django.urls import reverse
import pytz
from django.dispatch import receiver
from django.db.models.signals import post_save

class QuoteList(models.Model):
    name = models.CharField(max_length=50, default='관리자') # 명언을 말한 사람의 이름
    original = models.CharField(max_length=150, default='Out of this World') # 명언의 원문
    translated = models.CharField(max_length=150, default='이승탈출') # 명언의 번역문
    added_date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'quote'
        verbose_name_plural = 'quotes'
        db_table = 'quote_quotelist'
        # github 업로드 테스트

    def modify(self):
        self.added_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name