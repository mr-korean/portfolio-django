# -*- coding: UTF-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.moveto_main, name='quote'),
    url(r'^ajax/quote_download/$', views.quote_download, name='quote_download'),
    url(r'ajax/count_all_quote/$', views.count_all_quote, name='count_all_quote')
]