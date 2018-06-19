from django.shortcuts import render, get_object_or_404, redirect
from .models import QuoteList
from django.http import JsonResponse, HttpResponse
import json, pytz, random

def quote_download(request):
    allQuotes = QuoteList.objects.all()
    howMany = allQuotes.count()
    randomOrder = random.randint(0, howMany - 1)
    foundQuote = allQuotes[randomOrder]

    data = {
        'original': foundQuote.original,
        'translated': foundQuote.translated,
        'name': foundQuote.name,
        'selected': randomOrder
    }
    return JsonResponse(data)

def count_all_quote(request):
    allQuotes = QuoteList.objects.all()
    howMany = allQuotes.count()
    data = {'counted' : howMany}
    return JsonResponse(data)

def moveto_main(request):
    return redirect('/')