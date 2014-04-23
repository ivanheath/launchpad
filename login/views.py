from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from main.views import main as homepage

def index(request):
    if request.user.is_authenticated():
	return homepage(request)
    else:
        return render(request, 'login/index.html')

def authenticater(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
	if user.is_active:
	    login(request, user)
	    return homepage(request)
	else:
	    return HttpResponse("fail")
    else:
	return HttpResponse("login failed")

def logout_now(request):
    logout(request)
    return index(request)
