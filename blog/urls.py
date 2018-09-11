# -*- coding: UTF-8 -*-

from django.conf.urls import url
from blog.views import *

urlpatterns = [
    url(r'^$', NoteLV.as_view(), name='index'),
    url(r'^note/$', NoteLV.as_view(), name='note_list'),

    url(r'^note/(?P<slug>[-\w]+)/$', NoteDV.as_view(), name='note_detail'),

    # 날짜별 아카이브
    url(r'^archive/$', NoteAV.as_view(), name='note_archive'),
    url(r'^(?P<year>\d{4})/$', NoteYAV.as_view(), name='note_year_archive'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/$', NoteMAV.as_view(month_format='%m'), name='note_month_archive'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{1,2})/$', NoteDAV.as_view(), name='note_day_archive'),
    url(r'^today/$', NoteTAV.as_view(), name='note_today_archive'),

    # 태그 관련
    url(r'^tag/$', TagCloud.as_view(), name='tag_cloud'),
    url(r'^tag/(?P<tag>[^/]+(?u))/$', NoteTOL.as_view(), name='tagged_object_list'),

    # 게시물 편집 관련
    url(r'^search/$', NoteSearch.as_view(), name='note_search'),
    url(r'^add/$', NoteCreate.as_view(), name = "note_add"),
    url(r'^change/$', NoteChange.as_view(), name = "note_change"),
    url(r'^(?P<pk>[0-9]+)/update/$', NoteUpdate.as_view(), name = "note_update"),
    url(r'^(?P<pk>[0-9]+)/delete/$', NoteDelete.as_view(), name = "note_delete"),
]