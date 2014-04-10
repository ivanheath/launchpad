from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from newsfeed.models import newsitem
from main.views import main
from django.utils import timezone
import datetime
from newsfeed import signals

def newspostform(request):
    if request.user.is_authenticated():
	username = request.user.username
	return render(request, 'newsfeed/post.html')

def posttonews(request):
    if request.user.is_authenticated():
	username = request.user.username
	title = request.POST.get('title')
	newstext = request.POST.get('newstext')
	now = datetime.datetime.now()
	if title == '':
	    return HttpResponse('please enter in a title for your fancy little news post')
	elif newstext == '':
	    return HttpResponse('your fancy little news post needs a news post, please type news into your news')
	else:
	    addnews = newsitem(user_name=username, news_title=title, news_body=newstext, pub_date=now)
	    addnews.save()
	    return HttpResponseRedirect('http://10.15.14.102:3550')

