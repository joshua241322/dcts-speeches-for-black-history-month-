from django.contrib import admin
from .models import Speech

@admin.register(Speech)
class SpeechAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'title', 'program')
    list_filter = ('date',)
