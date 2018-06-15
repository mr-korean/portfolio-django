# -*- coding: UTF-8 -*-

from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
import pytz
from django.dispatch import receiver
from django.db.models.signals import post_save

class Record(models.Model):
    # 일반 기록만을 '계속' 저장. 모든 기록을 조회하고 싶을 때만 사용한다. (용량 걱정은 나중 문제)
    player = models.ForeignKey('auth.User')
    played_date = models.DateTimeField(default=timezone.now)
    gametitle = models.CharField(max_length=20, default='monte')
    score = models.IntegerField()
    level = models.PositiveSmallIntegerField(default = 1)

    def modify(self):
        self.played_date = timezone.now()
        self.save()

    def __str__(self):
        return self.gametitle

class HighRecord(models.Model):
    # 최고 기록만을 저장한다.
    # ※※※ 최고기록을 갱신하는 과정은 여기가 아닌, 올려보내기 전 단계(즉 AJAX)에서 한다.
    player = models.ForeignKey('auth.User')
    played_date = models.DateTimeField(default=timezone.now)
    gametitle = models.CharField(max_length=20, default='monte')
    highscore = models.PositiveSmallIntegerField()
    level = models.PositiveSmallIntegerField(default = 1)

    def modify(self):
        self.played_date = timezone.now()
        self.save()

    def __str__(self):
        return self.gametitle

# 나중에 gametitle도 auth.User처럼 ForeignKey를 이용해 다르게 적용할 수 있다.