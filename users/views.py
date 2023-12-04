# from django.shortcuts import render
from django.urls import reverse, reverse_lazy
# from django.http import HttpResponse, HttpResponseRedirect
# from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, UpdateView
# from django.contrib.auth.forms import AuthenticationForm
from .forms import LoginUserForm, RegisterUserForm, ProfileUserForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model

# -------------------------------------------------

class LoginUser(LoginView):
	form_class = LoginUserForm
	template_name = 'users/login.html'
	extra_context = {
		'title': 'Авторизация',
	}


class RegisterUser(CreateView):
	form_class = RegisterUserForm
	template_name = 'users/register.html'
	extra_context = {
		'title': 'Регистрация',
	}
	success_url = reverse_lazy('users:login')


class ProfileUser(LoginRequiredMixin, UpdateView):
	model = get_user_model()
	form_class = ProfileUserForm
	template_name = 'users/profile.html'
	extra_context = {
		'title': 'Профиль пользователя',
	}

	def get_success_url(self):
		# return reverse_lazy('users:profile', args=[self.request.user.pk])
		return reverse_lazy('users:profile')

	def get_object(self, queryset=None):
		return self.request.user
