from django.contrib import admin
from .models import Entry


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'preview', 'view_counter',)
    search_fields = ('id', 'title', 'content',)
