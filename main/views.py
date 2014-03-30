from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

def main(request):
    if request.user.is_authenticated():
	username = request.user.username
        return render(request, 'main/main.html',
	    {"username":username,
	    })
    else:
	return HttpResponse("nope")
