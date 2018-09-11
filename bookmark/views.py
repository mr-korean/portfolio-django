# -*- coding: UTF-8 -*-

from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from mysite.views import LoginRequiredMixin

# Create your views here.

class BookmarkList(ListView):
    model = Bookmark

class BookmarkDetail(DetailView):
    model = Bookmark

class BookmarkCreate(LoginRequiredMixin, CreateView):
    model = Bookmark
    fields = ['title', 'url', 'info', 'description']
    success_url = reverse_lazy('bookmark:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(BookmarkCreate, self).form_valid(form)
    
class BookmarkChange(LoginRequiredMixin, ListView):
    template_name = 'bookmark/bookmark_change_list.html'

    def get_queryset(self):
        return Bookmark.objects.filter(owner = self.request.user)

class BookmarkUpdate(LoginRequiredMixin, UpdateView):
    model = Bookmark
    fields = ['title', 'url', 'info', 'description']
    success_url = reverse_lazy('bookmark:index')

class BookmarkDelete(LoginRequiredMixin, DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark:index')