# -*- coding: UTF-8 -*-

from django.conf.urls import url
from blog.views import *

urlpatterns = [
    url(r'^$', NoteLV.as_view(), name='index'),
    url(r'^note/$', NoteLV.as_view(), name='note_list'),

    url(r'^note/(?P<slug>[-\w]+)/$', NoteDV.as_view(), name='note_detail'),

    # 날짜별 아카이브 링크
    url(r'^archive/$', NoteAV.as_view(), name='note_archive'),
    url(r'^(?P<year>\d{4})/$', NoteYAV.as_view(), name='note_year_archive'),
    url(r'^(?P<year>\d{4})/(?P<month>[-\w]{2,3})/$', NoteMAV.as_view(), name='note_month_archive'),
    url(r'^(?P<year>\d{4})/(?P<month>[-\w]{2,3})/(?P<day>\d{1,2})/$', NoteDAV.as_view(), name='note_day_archive'),
    url(r'^today/$', NoteTAV.as_view(), name='note_today_archive'),
]