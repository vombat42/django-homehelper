from django.contrib import admin
from .models import *

# ----------------------------------------

class DeadlineFilter(admin.SimpleListFilter):
    title = 'Срок выполнения'
    parameter_name = 'is_deadline'

    def lookups(self, request, model_admin):
        return [
            ('yes','Есть'),
            ('no','Нет'),
        ]

    def queryset(self, request, queryset):
        if self.value() == 'yes':
            return queryset.filter(time_deadline__isnull=False)
        elif self.value() == 'no':
            return queryset.filter(time_deadline__isnull=True)
            


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
	# формируем поле "slug" автоматически из полей "title" и "category"
    prepopulated_fields = {"slug": ("title", "category",)}
    list_display = ('id', 'title', 'category', 'status', 'time_create', 'time_deadline',)
    list_display_links = ('id', 'title', 'category',)
    list_editable = ('status',)
    list_per_page = 10
    search_fields = ('title','category__name',)
    list_filter = (DeadlineFilter, 'category__name','status',)
    save_on_top = True

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # Поле slug будет заполнено на основе поля "name"
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


# admin.site.register(Task, TaskAdmin)
# admin.site.register(Category, CategoryAdmin)

