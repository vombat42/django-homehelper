from django.shortcuts import render
from django.http import HttpResponse

# -------------------------------------------------

def index(request):
	return HttpResponse('Words Main')
	# return render(request, 'users/login.html', data)

def help(request):
	return HttpResponse('Words Help')
	# return render(request, 'users/login.html', data)

def about(request):
	return HttpResponse('Words About')
	# return render(request, 'users/logout.html', data)
	