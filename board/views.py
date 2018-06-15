# -*- coding: UTF-8 -*-

from django.shortcuts import render
# django.views.generic 는 데이터를 보여주기 위한 사전에 정의된 뷰이다. 일반적으로 프로젝트에서 많이 사용되는 뷰가 있다.
from django.views.generic import ListView, DetailView, TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from board.models import Post

# Create your views here.
class PostList(ListView):
    model = Post
    # template_name = 'board/post_list.html'
    context_object_name = 'posts'
    # https://goo.gl/BRFiJV 페이지당 표시해야 할 객체의 수를 지정
    paginate_by = 10

class PostDetail(DetailView):
    # url의 파라미터에서 pk값을 추출하여 사용 현재 게시물을 확인
    model = Post
    context_object_name = 'post'

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    success_url = reverse_lazy('board:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(PostCreate, self).form_valid(form)