# -*- coding: UTF-8 -*-

from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView, TodayArchiveView
from .models import Note
from tagging.models import Tag, TaggedItem # 태그 관련 모델(설치해야 가능)
from tagging.views import TaggedObjectList # 태그 관련 뷰(설치해야 가능)

class NoteLV(ListView):
    model = Note
    template_name = 'blog/note_all.html'
    context_object_name = 'notes' # 템플릿에서 사용될 변수명
    paginate_by = 5 # 한 페이지에 보여주는 목록의 최대 개수

class NoteDV(DetailView):
    model = Note

class TagCloud(TemplateView):
    template_name = 'tagging/tagging_cloud.html'

class NoteTOL(TaggedObjectList):
    model = Note
    template_name = 'tagging/tagging_note_list.html'

# 날짜별 아카이브 뷰

class NoteAV(ArchiveIndexView):
    model = Note
    date_field = 'modify_date' # 테이블에서 객체 리스트를 가져온 후, modify_date를 기준으로 최신 객체를 먼저 출력(이라고 함. 필요한가?)

class NoteYAV(YearArchiveView):
    model = Note
    date_field = 'modify_date'
    make_object_list = True

class NoteMAV(MonthArchiveView):
    model = Note
    date_field = 'modify_date'

class NoteDAV(DayArchiveView):
    model = Note
    date_field = 'modify_date'

class NoteTAV(TodayArchiveView):
    model = Note
    date_field = 'modify_date'

