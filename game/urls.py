# -*- coding: UTF-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.MainView.as_view(), name='index'),
    url(r'game-(?P<order>[0-9]+)/$', views.show_game, name='show_game'),
    url(r'^leaderboard/', views.leaderboard, name='leaderboard'),

    url(r'^ajax/score_upload_monte/$', views.score_upload_monte, name='score_upload_monte'),
    url(r'^ajax/highscore_upload_monte/$', views.highscore_upload_monte, name='highscore_upload_monte'),
    url(r'^ajax/record_download_monte/$', views.record_download_monte, name='record_download_monte'),
]