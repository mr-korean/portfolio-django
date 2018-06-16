# -*- coding: UTF-8 -*-

from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Record, HighRecord
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
import json, pytz

# 장고 쿼리셋에 관해서는
# (1) http://pythonstudy.xyz/python/article/310-Django-%EB%AA%A8%EB%8D%B8-API
# (2) http://brownbears.tistory.com/63
# (3) https://docs.djangoproject.com/en/2.0/topics/db/queries/
# (4) http://raccoonyy.github.io/using-django-querysets-effectively-translate/
# 위의 링크를 참고할 것.

class MainView(TemplateView):
    template_name = 'game/game_main.html'

def show_game(request, order):
    gamenumber = str(order)
    return render(request, 'game/game-' + gamenumber + '.html')


def leaderboard(request):
    # ※ 일반기록과 최고점수를 분리했으므로, 이제 랭킹에는 최고점수만을 표시해야 함.
    # (1) 최고점수 내림차순, (2) 날짜 최신 순으로 정렬할 것.
    checkedRecords = HighRecord.objects.all()
    records_monte = checkedRecords.order_by('-highscore')[:10] # Top 10 제한 (필터링 & 정렬 단계에서 해야 함)
    return render(request, 'game/game_score.html', {'records_monte' : records_monte})

@login_required
def score_upload_monte(request):
    gotScore = request.GET.get('uploadedScore', None)
    localId = request.user.id
    foundUser = User.objects.get(id = localId)
    
    Record.objects.create(player = foundUser, gametitle = 'monte', score = gotScore)

    data = {
        'message': "점수가 서버에 등록되었답니다."
    }
    return JsonResponse(data)

@login_required
def highscore_upload_monte(request):
    gotHighscore = request.GET.get('uploadedHighscore', None)
    localId = request.user.id
    foundUser = User.objects.get(id = localId)

    HighRecord.objects.create(player = foundUser, gametitle = 'monte', highscore = gotHighscore)
    # ※※※ (단, 현재는 기존 기록과 관계없이 새로 만들기만 하므로 나중에 불러오면 전부 불러오게 된다. 뿌려줄 때 필터링하면 되는 것인가?)

    data = {
        'message': "최고점수가 서버에 등록되었답니다."
    }
    return JsonResponse(data)

@login_required
def record_download_monte(request):
    localId = request.user.id
    foundUser = User.objects.get(id = localId)
    record = Record.objects.all()
    highrecord = HighRecord.objects.all()

    latestRecord = record.filter(player = foundUser).filter(gametitle = 'monte').order_by('-played_date')[0]
    latestHighRecord = highrecord.filter(player = foundUser).filter(gametitle = 'monte').order_by('-played_date')[0]

    data = {
        'score':latestRecord.score,
        'highScore':latestHighRecord.highscore
    }
    return JsonResponse(data)