from django.contrib import admin
from .models import *

# ----------------------------------------

@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'chapter', 'pic', 'voice',)
	list_display_links = ('name',)
	list_per_page = 10
	search_fields = ('name','chapter',)
	list_filter = ('chapter',)
	save_on_top = True

@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')
	list_display_links = ('name',)

@admin.register(WordSet)
class WordSetAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')
	list_display_links = ('name',)