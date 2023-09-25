from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework import generics
from .models import Tasks
from .serializers import TasksSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# --------------------------------------

menu = [
	{'title':'Задачи', 'url_name': 'tasks_main'},
	{'title':'О приложении', 'url_name': 'tasks_about'},
	{'title':'Помощь', 'url_name': 'tasks_help'},
	{'title':'API', 'url_name': 'tasks_apiview'},
	{'title':'Админка', 'url_name': 'admin:index'},
]

def index(request):
	tasks = Tasks.objects.all()
	data = {
		'title': 'tasks main',
		'styles': 'tasks/css/styles.css',
		'menu': menu,
		'tasks': tasks,
	}
	return render(request, 'tasks/index.html', data)


def show_one_task(request, task_id):
	task = get_object_or_404(Tasks, pk=task_id)
	data = {
		'title': 'task details',
		'styles': 'tasks/css/styles.css',
		'menu': menu,
		'task' : task,
	}
	return render(request, 'tasks/details.html', data)


def help(request):
	data = {
		'title':'help tasks',
		'styles':'tasks/css/styles.css',
		'menu': menu,
	}
	return render(request, 'tasks/help.html', data)

def about(request):
	data = {
		'title':'about tasks',
		'styles':'tasks/css/styles.css',
		'menu': menu,
	}
	return render(request, 'tasks/about.html', data)

class TasksAPIViewList(generics.ListCreateAPIView):
	queryset = Tasks.objects.all()
	serializer_class = TasksSerializer	

class TasksAPIView(APIView):
	queryset = Tasks.objects.all()
	serializer_class = TasksSerializer

	def get(self, request):
		w = Tasks.objects.all()
		return Response({'posts': TasksSerializer(w, many=True).data})

	def post(self, request):
		serializer = TasksSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		
		return Response({'post': serializer.data})


	def put(self, request, *args, **kwargs):
		pk = kwargs.get("pk", None)
		if not pk:
			return Response({"error": "Method PUT not allowed"})

		try:
			instance = Women.objects.get(pk=pk)
		except:
			return Response({"error": "Object does not exists"})

		serializer = TasksSerializer(data=request.data, instance=instance)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response({"post": serializer.data})