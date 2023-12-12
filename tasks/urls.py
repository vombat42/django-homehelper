from django.urls import path, include
from . import views
from rest_framework import routers

# --------------------------------------

router = routers.SimpleRouter()
router.register(r'tasks', views.TasksAPIViewSet, basename='tasks')


urlpatterns = [
    path('', views.TasksList.as_view(), name='tasks-main'),
    path('help/', views.help, name='tasks-help'),
    path('about/', views.about, name='tasks-about'),
    path('taskadd/', views.TasksCreate.as_view(), name='tasks-add'),
    path('<int:task_id>/', views.show_one_task, name='task-details'),
    # path('api/v1/taskslist', views.TasksAPIViewList.as_view(), name='tasks_api_view'),
    # path('api/v1/taskslist/<int:pk>', views.TasksAPIUpdate.as_view(), name='tasks_api_update'),
    # path('api/v1/tasksdetail/<int:pk>', views.TasksAPIDetailView.as_view(), name='tasks_api_detail_view'),
    path('api/v1/', include(router.urls)),
    # path('api/v1/taskslist', views.TasksAPIViewSet.as_view({'get': 'list'}), name='tasks_api_view'),
    # path('api/v1/taskslist/<int:pk>', views.TasksAPIViewSet.as_view({'put': 'update'}), name='tasks_api_update'),
]