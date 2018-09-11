# -*- coding: UTF-8 -*-

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Bookmark(models.Model):
    title = models.CharField('제목', max_length = 100, blank = True, null = True)
    url = models.URLField('URL', unique = True)
    info = models.CharField('한줄요약', max_length=100, blank = True)
    description = models.TextField('설명', blank = True)
    create_date = models.DateTimeField('등록일', default = timezone.now)
    modify_date = models.DateTimeField('수정일', default = timezone.now)
    owner = models.ForeignKey(User, null = True, help_text="작성자")

    class Meta:
        ordering = ('-modify_date', )

    def __str__(self):
        return self.title