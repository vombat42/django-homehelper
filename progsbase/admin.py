from django.contrib import admin
from .models import *
# ----------------------------------------------------



class ProgImageInline(admin.TabularInline):
    """Список изображений программы"""
    model = ProgImage
    extra = 0


class ProgLinkInline(admin.TabularInline):
    """Список ссылок программы"""
    model = ProgLink
    extra = 0


@admin.register(Prog)
class ProgAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title", "author",)} # формируем поле "slug" автоматически из полей "title" и "author"
    list_display = ('id', 'title', 'lang', 'author','time_create',)
    list_display_links = ('id', 'title', 'author',)
    # list_editable = ('title',)
    list_per_page = 10
    search_fields = ('title',)
    # list_filter = (DeadlineFilter, 'category__name','status',)
    save_on_top = True
    inlines = [ProgImageInline, ProgLinkInline,] # список изображений программы


@admin.register(Lang)
class LangAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)} # формируем поле "slug" автоматически из поля "name"
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)} # формируем поле "slug" автоматически из поля "name"
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
