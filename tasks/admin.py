from django.contrib import admin
from .models import *

# ----------------------------------------

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
	# формируем поле "slug" автоматически из полей "title" и "category"
    prepopulated_fields = {"slug": ("title", "category",)}
    list_display = ('id', 'title', 'category', 'status', 'time_create', 'time_deadline')
    list_display_links = ('id', 'title', 'category')
    list_editable = ('status',)
    list_per_page = 10

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # Поле slug будет заполнено на основе поля "name"
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


# admin.site.register(Task, TaskAdmin)
# admin.site.register(Category, CategoryAdmin)

