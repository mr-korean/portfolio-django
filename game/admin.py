from django.contrib import admin
from .models import Record, HighRecord

# Register your models here.
class RecordAdmin(admin.ModelAdmin):
    list_display = ('player', 'gametitle', 'score', 'played_date')
admin.site.register(Record, RecordAdmin)

class HighRecordAdmin(admin.ModelAdmin):
    list_display = ('player', 'gametitle', 'highscore', 'played_date')
admin.site.register(HighRecord, HighRecordAdmin)