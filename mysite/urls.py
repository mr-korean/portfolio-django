# -*- coding: UTF-8 -*-

"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.conf.urls.static import static #사진 앱(p.216)
from django.conf import settings #사진 앱(p.216)

from django.contrib import admin
from django.contrib.auth import views
from mysite.views import HomeView, UserRegisterView, UserRegisterDoneView, validate_username
from game import urls
from blog import urls
from board import urls
from quote import urls
from bookmark import urls

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^admin/', admin.site.urls),

    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),
    url(r'^accounts/register/$', UserRegisterView.as_view(), name='register'),
    url(r'^accounts/register/done/$', UserRegisterDoneView.as_view(), name='register_done'),

    url(r'^ajax/validate_username/$', validate_username, name="validate_username"),
    
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^board/', include('board.urls', namespace='board')),
    url(r'^game/', include('game.urls', namespace='game')),
    url(r'^quote/', include('quote.urls', namespace='quote')),
    url(r'^photo/', include('photo.urls', namespace='photo')),
    url(r'^bookmark/', include('bookmark.urls', namespace='bookmark')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
# static 함수가 반환하는 URL 패턴도 추가