# -*- coding: UTF-8 -*-

from django.contrib import admin
from blog.models import Note

class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'modify_date') # 장고 관리 페이지에서 보여줄 정보들
    list_filter = ('modify_date',) # 필터 사이드바 사용
    search_fields = ('title', 'content') # 검색창 사용
    prepopulated_fields = {'slug': ('title',)} # slug에 title을 자동으로 적용

admin.site.register(Note, NoteAdmin) # 관리 페이지에 NoteAdmin의 설정을 적용