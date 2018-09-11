# -*- coding: UTF-8 -*-

from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView, TodayArchiveView
from .models import Note
from tagging.models import Tag, TaggedItem # 태그 관련 모델(설치해야 가능)
from tagging.views import TaggedObjectList # 태그 관련 뷰(설치해야 가능)

from django.views.generic.edit import FormView # 검색폼
from blog.forms import NoteSearchForm # 자작 검색폼
from django.db.models import Q # 검색용 Q 클래스
from django.shortcuts import render # 검색용 단축 함수

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from mysite.views import LoginRequiredMixin


class NoteLV(ListView):
    model = Note
    template_name = 'blog/note_list.html'
    context_object_name = 'notes' # 템플릿에서 사용될 변수명
    paginate_by = 5 # 한 페이지에 보여주는 목록의 최대 개수

class NoteDV(DetailView):
    model = Note

class TagCloud(TemplateView):
    template_name = 'tagging/tagging_cloud.html'

class NoteTOL(TaggedObjectList):
    model = Note
    template_name = 'tagging/tagging_note_list.html'

# 날짜별 아카이브 뷰

class NoteAV(ArchiveIndexView):
    model = Note
    date_field = 'modify_date' # 테이블에서 객체 리스트를 가져온 후, modify_date를 기준으로 최신 객체를 먼저 출력(이라고 함. 필요한가?)

class NoteYAV(YearArchiveView):
    model = Note
    date_field = 'modify_date'
    make_object_list = True

class NoteMAV(MonthArchiveView):
    model = Note
    date_field = 'modify_date'

class NoteDAV(DayArchiveView):
    model = Note
    date_field = 'modify_date'

class NoteTAV(TodayArchiveView):
    model = Note
    date_field = 'modify_date'

class NoteSearch(FormView):
    form_class = NoteSearchForm
    template_name = 'blog/note_search.html'

    def form_valid(self, form):
        schWord = '%s' % self.request.POST['search_word']
        # (아마도 템플릿의) POST 요청으로 온 값을 변수 schWord에 저장
        note_list = Note.objects.filter(Q(title__icontains=schWord) | Q(slug__icontains=schWord) | Q(description__icontains=schWord) | Q(content__icontains=schWord)).distinct()
        # 모델 Note를 schWord를 통해 샅샅이 뒤짐(icontains는 대소문자 가리지 않음)

        context = {} # 템플릿에 넘겨줄 변수 context를 아래와 같이 정의함
        context['form'] = form # form 객체를 변수 form에 저장
        context['search_term'] = schWord # schWord의 값을 변수 search_term에 저장
        context['object_list'] = note_list # 상동

        return render(self.request, self.template_name, context)
        # 위의 결과를 반환함(이게 없으니까 에러가 나지)

class NoteCreate(LoginRequiredMixin, CreateView):
    model = Note
    fields = ['title', 'description', 'content', 'tag']
    #initial = {'slug' : '자동으로-추가되므로-입력-금지'}
    success_url = reverse_lazy('blog:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(NoteCreate, self).form_valid(form)

class NoteChange(LoginRequiredMixin, ListView):
    template_name = 'blog/note_change_list.html'

    def get_queryset(self):
        return Note.objects.filter(owner = self.request.user)

class NoteUpdate(LoginRequiredMixin, UpdateView):
    model = Note
    fields = ['title', 'description', 'content', 'tag']
    success_url = reverse_lazy('blog:index')

class NoteDelete(LoginRequiredMixin, DeleteView):
    model = Note
    success_url = reverse_lazy('blog:index')