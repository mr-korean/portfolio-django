# -*- coding: UTF-8 -*-

from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark

# Create your views here.

class BookmarkList(ListView):
    model = Bookmark

class BookmarkDetail(DetailView):
    model = Bookmark