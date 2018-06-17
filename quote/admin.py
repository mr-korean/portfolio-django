from django.contrib import admin
from .models import QuoteList

# Register your models here.
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('name', 'original', 'translated', 'added_date', 'modified_date')
admin.site.register(QuoteList, QuoteAdmin)