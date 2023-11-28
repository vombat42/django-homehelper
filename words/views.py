from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView #, FormView
# from django.views import View
# from .forms import SelectSetForm
from .models import *
import json

# -------------------------------------------------

menu = [
	{'title':'Слова', 'url_name': 'words_main'},
	{'title':'Занятие', 'url_name': 'words_select_set'},
	{'title':'О приложении', 'url_name': 'words_about'},
	{'title':'Помощь', 'url_name': 'words_help'},
]


def index(request):
	# form = SelectSetForm()
	data = {
		'title': 'words main',
		'styles': 'words/css/styles.css',
		'menu': menu,
		# 'form': form,
	}
	return render(request, 'words/index.html', data)


class SelectSet(ListView):
	model = WordSet
	template_name = 'words/select_set.html'
	context_object_name = 'word_set'
	extra_context = {
		'title': 'words select set',
		'styles': 'words/css/styles.css',
		'menu': menu,
	}

	# def get_queryset(self):
		# return WordSet.objects.all()


def exercise(request):
	qs = set()
	for key, value in request.POST.items():
		if key[0:3] == 'set':
			qs.update(list(WordSet.objects.get(pk=int(value)).words.all()))
	data = {
		'title': 'words exercise',
		'styles': 'words/css/styles.css',
		'menu': menu,
		'words' : qs,
		# 'wjjj' : json.dumps(qs)
	}
	return render(request, 'words/exercise.html', data)


def help(request):
	return HttpResponse('Words Help')
	# return render(request, 'users/login.html', data)


def about(request):
	return HttpResponse('Words About')
	# return render(request, 'users/logout.html', data)
	