from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from .models import *
from django.views.generic import ListView, DetailView
# import settings
# -----------------------------------------------------------

menu = [
	{'title':'Программы', 'url_name': 'progs-main'},
	# {'title':'Добавить задачу', 'url_name': 'tasks-add'},
	{'title':'О приложении', 'url_name': 'progs-about'},
	{'title':'Помощь', 'url_name': 'progs-help'},
	{'title':'Админка', 'url_name': 'admin:index'},
	# {'title':'API', 'url_name': 'tasks-list'},
]

class ProgsList(ListView):
	"""Список программ"""
	model = Prog
	template_name = 'progsbase/index.html'
	context_object_name = 'progsbase'
	extra_context = {
		'title': 'progsbase main',
		'styles': 'progsbase/css/styles.css',
		'menu': menu,
	}


class ProgsDetails(DetailView):
	"""Полная информация об выбранной программе"""
	model = Prog
	template_name = 'progsbase/prog_details.html'
	context_object_name = 'prog'
	slug_url_kwarg = 'prog_slug'
	# extra_context = {
		# 'title': 'prog details',
		# 'styles': 'progsbase/css/styles.css',
	# }

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Prog Details'
		context['styles'] = 'progsbase/css/styles.css'
		context['menu'] = menu
		img_id = Prog.objects.get(slug=self.kwargs['prog_slug']) # по слагу определяем id программы
		context['images'] = ProgImage.objects.filter(prog_id=img_id) # отбираем картинки по id программы
		context['links'] = ProgLink.objects.filter(prog_id=img_id) # отбираем ссылки по id программы
		# содержимое файла программы
		f_name = "."+img_id.text.url
		f = open(f_name, 'r')
		context['prog_text'] = f.read()
		f.close()
		return context

def taglist(request, tag_slug):
	return HttpResponse('Progs Tags - '+ tag_slug)


def langlist(request, lang_slug):
	return HttpResponse('Progs on - '+ lang_slug)


def help(request):
	return HttpResponse('Progs Help')


def about(request):
	return HttpResponse('Progs About')
	# return render(request, 'users/logout.html', data)