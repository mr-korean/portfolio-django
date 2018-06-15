# -*- coding: UTF-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.leaderboard, name='leaderboard'),
    url(r'^ajax/score_upload_monte/$', views.score_upload_monte, name='score_upload_monte'),
    url(r'^ajax/highscore_upload_monte/$', views.highscore_upload_monte, name='highscore_upload_monte'),
    url(r'^ajax/record_download_monte/$', views.record_download_monte, name='record_download_monte'),
]