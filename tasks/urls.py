from django.urls import path
from . import views

# --------------------------------------

urlpatterns = [
    path('', views.index, name='tasks_main'),
    path('help/', views.help, name='tasks_help'),
    path('about/', views.about, name='tasks_about'),
    # path('api/taskslist', views.TasksAPIView.as_view(), name='tasks_apiview'),
    path('api/taskslist', views.TasksAPIViewList.as_view(), name='tasks_apiview'),
]