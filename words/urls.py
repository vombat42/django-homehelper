from django.urls import path
from . import views

# --------------------------------------

urlpatterns = [
    path('', views.index, name='words_main'),
    path('help/', views.help, name='words_help'),
    path('about/', views.about, name='words_about'),
]