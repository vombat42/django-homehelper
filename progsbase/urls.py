from django.urls import path
from . import views
# --------------------------------------

urlpatterns = [
    path('', views.ProgsList.as_view(), name='progs-main'),
    path('prog/<slug:prog_slug>/', views.ProgsDetails.as_view(), name='prog-details'),
    path('tag/<slug:tag_slug>/', views.taglist, name='progs-tag'),
    path('lang/<slug:lang_slug>/', views.langlist, name='progs-lang'),
    path('help/', views.help, name='progs-help'),
    path('about/', views.about, name='progs-about'),
]
