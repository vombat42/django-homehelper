from django.apps import AppConfig


class ProgsbaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'progsbase'
    verbose_name = "База программ"
    # verbose_name_plural = "Задачи"