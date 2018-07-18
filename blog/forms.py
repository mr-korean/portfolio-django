from django import forms

class NoteSearchForm(forms.Form):
    search_word = forms.CharField(label = '검색어')