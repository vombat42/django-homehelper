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
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', index, name='main'),
    path('tasks/', include('tasks.urls')),
    path('words/', include('words.urls')),
    path('users/', include('users.urls', namespace='users')),
    # path('progs/', include('progsbase.urls', namespace='progsbase')),
    path('progsbase/', include('progsbase.urls')),
]

from .settings import DEBUG, MEDIA_URL, MEDIA_ROOT
if DEBUG:
    # add debug toolbar only for DEBUG mode
    urlpatterns.append(path("__debug__/", include("debug_toolbar.urls")))
    
    # for show media files in DEBUG mode
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)

# handler404 = 'django_homehelper.views.page_not_found'
handler404 = page_not_found

# Настройка админ панели
admin.site.site_header = 'Панель администрирования сайта'
admin.site.index_title = 'Приложения "Задачи" и "Слова"'
