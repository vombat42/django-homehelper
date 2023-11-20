from django.shortcuts import render
from django.http import HttpResponse

# -------------------------------------------------

def login(request):
	return HttpResponse('LogIn')
	# return render(request, 'users/login.html', data)

def logout(request):
	return HttpResponse('LogOut')
	# return render(request, 'users/logout.html', data)
	