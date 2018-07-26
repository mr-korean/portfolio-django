# -*- coding: UTF-8 -*-

from django.conf.urls import url
from photo.views import *

urlpatterns = [
    url(r'^$', AlbumListView.as_view(), name = 'index'),

    url(r'^album/$', AlbumListView.as_view(), name = 'album_list'),
    url(r'^album/(?P<pk>\d+)/$', AlbumDetailView.as_view(), name = 'album_detail'),
    url(r'^photo/(?P<pk>\d+)/$', PhotoDetailView.as_view(), name = 'photo_detail'),
]