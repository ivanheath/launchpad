from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from main.views import main

def index(request):
    return render(request, 'login/index.html')

def authenticater(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
	if user.is_active:
	    login(request, user)
	    return main(request)
	else:
	    return HttpResponse("fail")
    else:
	return HttpResponse("login failed")
