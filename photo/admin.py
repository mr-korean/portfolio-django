# -*- coding: UTF-8 -*-

from django.contrib import admin
from photo.models import Album, Photo

# Register your models here.

class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 2
    # StackedInline(열) 방식으로 이미지를 정렬

class AlbumAdmin(admin.ModelAdmin):
    inlines = [PhotoInline] # 위에서 사용한 정렬 방식을 사용
    list_display = ('name', 'description')

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'upload_date')

# 위의 설정을 모델에 덮어씌움
admin.site.register(Album, AlbumAdmin)
admin.site.register(Photo, PhotoAdmin)