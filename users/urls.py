from django.urls import path
from . import views

# --------------------------------------

app_name = 'users'

urlpatterns = [
    path('login/', views.login_user, name='users_login'),
    path('logout/', views.logout_user, name='users_logout'),

]