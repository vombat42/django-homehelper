from django.urls import path
from . import views

# --------------------------------------

urlpatterns = [
    path('', views.index, name='words_main'),
    path('set-select/', views.SelectSet.as_view(), name='words_select_set'),
    path('exercise/', views.exercise, name='words_exercise'),
    path('help/', views.help, name='words_help'),
    path('about/', views.about, name='words_about'),
]