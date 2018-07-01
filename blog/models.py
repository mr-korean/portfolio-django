# -*- coding: UTF-8 -*-

from django.db import models
from django.utils import timezone
from django.urls import reverse
from tagging.fields import TagField

class Note(models.Model):
    title = models.CharField('제목', max_length=50) # 관리 페이지에서 보여질 스트링은 한글 사용 가능 / CharField는 한 줄 전용
    slug = models.SlugField('키워드', unique=True, allow_unicode=True, help_text='제목 대신 쓰이는 한 단어.')
    description = models.CharField('설명', max_length=100, blank=True, help_text='간단한 설명.')
    content = models.TextField('내용') # TextField는 여러 줄 입력 가능
    create_date = models.DateTimeField('생성일', default=timezone.now)
    modify_date = models.DateTimeField('수정일', default=timezone.now)
    tag = TagField() # 태그를 입력하는 칸(교재 p.158)

    class Meta:
        verbose_name = 'note' # 테이블 별명(단수)
        verbose_name_plural = 'notes' # 테이블 별명(복수)
        db_table = 'blog_note' # DB에서의 테이블 이름(혼란 방지를 위해 이름은 건드리지 말 것)
        ordering = ('-modify_date', ) # modify_date 기준으로, 내림차순(- 사용)

    def __str__(self):
        return self.title # 장고 관리자 페이지에서 제목이 표시됨
    
    def get_absolute_url(self):
        return reverse('blog:note_detail', args=(self.slug,)) # 내용 보기 페이지(note_detail)로 이동

    def get_previous_post(self): # ※ post나 modify_date는 장고의 기능이므로 멋대로 이름 바꾸지 말 것
        try:
            return self.get_previous_by_modify_date()
        except Note.DoesNotExist:
            return None

    def get_next_post(self):
        try:
            return self.get_next_by_modify_date()
        except Note.DoesNotExist:
            return None        
