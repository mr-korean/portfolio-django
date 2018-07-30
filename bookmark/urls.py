# -*- coding: UTF-8 -*-

from django.conf.urls import url
from django.contrib import admin

from bookmark.views import *

urlpatterns = [
    url(r'^$', BookmarkList.as_view(), name='index'),
    url(r'^/(?P<pk>\d+)/$', BookmarkDetail.as_view(), name='detail'),
]