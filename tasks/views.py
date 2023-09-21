from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Tasks
from .serializers import TasksSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
# --------------------------------------

def index(request):
	data = {
		'title':'tasks main',
		'styles':'tasks/css/styles.css',
	}
	return render(request, 'tasks/index.html', data)


def help(request):
	return HttpResponse('<h1>Помощь по TASKS</h1>')


def about(request):
	return HttpResponse('<h1>About TASKS</h1>')


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