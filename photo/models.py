# -*- coding: UTF-8 -*-

from django.db import models
from django.core.urlresolvers import reverse

from photo.fields import ThumbnailImageField

# Create your models here.

class Album(models.Model):
    name = models.CharField(max_length = 50)
    description = models.CharField('한줄요약', max_length = 100, blank = True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('photo:album_detail', args = (self.id,))
        # 각각의 id를 찾아서 연결해 줌

class Photo(models.Model):
    album = models.ForeignKey(Album)
    title = models.CharField(max_length = 50)
    image = ThumbnailImageField(upload_to = 'photo/%Y/%m')
    description = models.TextField('사진 설명', blank = True)
    upload_date = models.DateTimeField('업로드 날짜', auto_now_add = True)

    class Meta:
        ordering = ['title']
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('photo:photo_detail', args = (self.id,))