from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from rest_framework import generics
from django.views.generic import ListView, CreateView
from .models import Task
from .forms import AddTaskForm
# from .urls import urlpatterns
from .serializers import TaskSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# --------------------------------------

menu = [
	{'title':'Задачи', 'url_name': 'tasks_main'},
	{'title':'Добавить задачу', 'url_name': 'tasks_add'},
	{'title':'О приложении', 'url_name': 'tasks_about'},
	{'title':'Помощь', 'url_name': 'tasks_help'},
	{'title':'API', 'url_name': 'tasks_apiview'},
	{'title':'Админка', 'url_name': 'admin:index'},
]

# def index(request):
# 	tasks = Task.objects.all()
# 	data = {
# 		'title': 'tasks main',
# 		'styles': 'tasks/css/styles.css',
# 		'menu': menu,
# 		'tasks': tasks,
# 	}
# 	return render(request, 'tasks/index.html', data)


class TasksList(LoginRequiredMixin, ListView):
	model = Task
	template_name = 'tasks/index.html'
	context_object_name = 'tasks'
	extra_context = {
		'title': 'tasks main',
		'styles': 'tasks/css/styles.css',
		'menu': menu,
	}


def show_one_task(request, task_id):
	task = get_object_or_404(Task, pk=task_id)
	data = {
		'title': 'task details',
		'styles': 'tasks/css/styles.css',
		'menu': menu,
		'task' : task,
	}
	return render(request, 'tasks/details.html', data)


# def add(request):
# 	if request.method == 'POST':
# 		form = AddTaskForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			return redirect('tasks_main')
# 	else:
# 		form = AddTaskForm()
	
# 	data = {
# 		'title': 'task details',
# 		'styles': 'tasks/css/styles.css',
# 		'menu': menu,
# 		'form': form,
# 	}
# 	return render(request, 'tasks/add.html', data)

# class TasksList(LoginRequiredMixin, DataMixin, CreateView):
class TasksCreate(LoginRequiredMixin, CreateView):
	form_class = AddTaskForm
	template_name = 'tasks/add.html'
	# success_url = reverse_lazy('tasks_main')
	extra_context = {
		'title': 'tasks details',
		'styles': 'tasks/css/styles.css',
		'menu': menu,
	}

	def form_valid(self, form):
		t = form.save(commit=False)
		t.author = self.request.user
		return super().form_valid(form)



def help(request):
	data = {
		'title':'help tasks',
		'styles':'tasks/css/styles.css',
		'menu': menu,
	}
	return render(request, 'tasks/help.html', data)


@login_required
def about(request):
	data = {
		'title':'about tasks',
		'styles':'tasks/css/styles.css',
		'menu': menu,
	}
	return render(request, 'tasks/about.html', data)


class TasksAPIViewList(generics.ListCreateAPIView):
	queryset = Task.objects.all()
	serializer_class = TaskSerializer	


class TasksAPIView(APIView):
	queryset = Task.objects.all()
	serializer_class = TaskSerializer

	def get(self, request):
		w = Task.objects.all()
		return Response({'posts': TaskSerializer(w, many=True).data})

	def post(self, request):
		serializer = TaskSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		
		return Response({'post': serializer.data})


	def put(self, request, *args, **kwargs):
		pk = kwargs.get("pk", None)
		if not pk:
			return Response({"error": "Method PUT not allowed"})

		try:
			instance = Task.objects.get(pk=pk)
		except:
			return Response({"error": "Object does not exists"})

		serializer = TaskSerializer(data=request.data, instance=instance)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response({"post": serializer.data})