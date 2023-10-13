"""
URL configuration for django_homehelper project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import index, page_not_found

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', index, name='main'),
    path('tasks/', include('tasks.urls')),
]

# add debug toolbar only for DEBUG mode
from .settings import DEBUG
if DEBUG:
    urlpatterns.append(path("__debug__/", include("debug_toolbar.urls")))
    print ('************************')

# handler404 = 'django_homehelper.views.page_not_found'
handler404 = page_not_found

# Настройка админ панели
admin.site.site_header = 'Панель администрирования сайта'
admin.site.index_title = 'Приложение "Задачи"'
