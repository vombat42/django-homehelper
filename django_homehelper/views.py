from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# --------------------------------------

def index(request):
	data = {
		'title':'Главная',
		'styles':'main/css/styles.css',
	}
	return render(request, 'main/index.html', data)


def page_not_found(request, exception=None):
	return HttpResponseNotFound('Упс, страница не найдена')
