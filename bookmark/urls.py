# -*- coding: UTF-8 -*-

from django.conf.urls import url
from django.contrib import admin

from bookmark.views import *

urlpatterns = [
    # 메인 페이지 & 세부사항 확인
    url(r'^$', BookmarkList.as_view(), name = 'index'),
    url(r'^(?P<pk>\d+)/$', BookmarkDetail.as_view(), name = 'detail'),

    # 게시물 편집
    url(r'^add/$', BookmarkCreate.as_view(), name = "add"),
    url(r'^change/$', BookmarkChange.as_view(), name = "change"),
    url(r'^(?P<pk>[0-9]+)/update/$', BookmarkUpdate.as_view(), name = "update"),
    url(r'^(?P<pk>[0-9]+)/delete/$', BookmarkDelete.as_view(), name = "delete"),
]