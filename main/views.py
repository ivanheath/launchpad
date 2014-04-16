from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from newsfeed.models import newsitem

def main(request):
    if request.user.is_authenticated():
	username = request.user.username
	currentnews = newsitem.objects.filter().order_by('-pub_date')[:10]
	return render(request, 'main/main.html',
	    {"username":username,
	     "currentnews":currentnews,
	    })

    else:
	return HttpResponse("nope")

def news_added(sender, instance, signal, *args, **kwargs):
    return main(request)

