from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from newsfeed.models import newsitem
from main.views import main
import datetime
from login.views import index
from main.views import main as homepage

def newspostform(request):
    if request.user.is_authenticated():
	username = request.user.username
	return render(request, 'newsfeed/post.html',
		     {"username":username,
		     })
    else:
	return index(request)

def posttonews(request):
    if request.user.is_authenticated():
	username = request.user.username
	title = request.POST.get('title')
	newstext = request.POST.get('newstext')
	now = datetime.datetime.now()
	receiver = request.POST.get('receiver')
	if title == '':
	    return HttpResponse('please enter in a title for your fancy little news post')
	elif newstext == '':
	    return HttpResponse('your fancy little news post needs a news post, please type news into your news')
	else:
	    addnews = newsitem(user_name=username, news_title=title, news_body=newstext, pub_date=now, receiver_name=receiver)
	    addnews.save()
	    return homepage(request)
    else:
	return index(request)

def message(request):
    if request.user.is_authenticated():
	username = request.user.username
	users = User.objects.filter().distinct()
	temp = "all users: "
	for i in users:
	    temp = temp + i.username + ", "
	return render(request, 'newsfeed/message.html',
		{"username":username,
		 "users":users,
		 "temp": temp,
		})
    else:
	return index(request)

def delete(request):
    if request.user.is_authenticated():
	username = request.user.username
	newsitems = newsitem.objects.filter(user_name = username).order_by('-pub_date')
	return render(request, 'newsfeed/delete.html',
		{"username":username,
		 "newsitems":newsitems,
		})
    else:
	return index(request)

def postdeleted(request):
    if request.user.is_authenticated():
	username = request.user.username
	newsid = request.POST.get("newsid")
	newstodelete = newsitem.objects.filter(id=request.POST.get("newsid"))
	newstodelete.delete()
	return homepage(request)
    else:
	return index(request)
