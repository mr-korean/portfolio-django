# -*- coding: UTF-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    # auto_now_add와 auto_now의 사용법은 https://goo.gl/GKVaAa 에서 DateTimeField를 참고
    title = models.CharField('제목', max_length=50)
    content = models.TextField('내용', blank=True)
    create_date = models.DateTimeField('생성일', auto_now_add=True)
    modify_date = models.DateTimeField('수정일', auto_now=True)
    owner = models.ForeignKey('auth.User', null=True)
        
    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        db_table  = 'board_posts'
        ordering  = ('-create_date',)
        
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # reverse에서 인자로 리스트를 전달하고자 하는 경우는 args=[1,5]
        return reverse('board:post_detail', kwargs={'pk':self.id})

    def get_previous_post(self):
        # get_previous_by_<필드명> 메서드
        try:
            return self.get_previous_by_create_date()
        except Post.DoesNotExist:
            return None

    def get_next_post(self):
        # get_next_by_<필드명> 메서드
        try:
            return self.get_next_by_create_date()
        except Post.DoesNotExist:
            return None