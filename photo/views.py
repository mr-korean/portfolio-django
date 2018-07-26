# -*- coding: UTF-8 -*-

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from photo.models import Album, Photo

# Create your views here.

class AlbumListView(ListView):
    model = Album

class AlbumDetailView(DetailView):
    model = Album

class PhotoDetailView(DetailView):
    model = Photo