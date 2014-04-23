from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from main.views import main as homepage
from login.views import index

def main(request):
    if request.user.is_authenticated():
	username = request.user.username
	test = request.user
	return render(request, 'edituser/edituser.html',
			{'username':username,
			 "userdetails":test,
			})
    else:
	return index(request)

def savechanges(request):
    if request.user.is_authenticated():
	user = request.user
	user.first_name = request.POST.get('firstname')
	user.last_name = request.POST.get('lastname')
	user.email = request.POST.get('email')
	user.save()
	username = request.user.username
	return homepage(request)
    else:
	return index(request)

def changepassword(request):
    if request.user.is_authenticated():
	user = request.user
	return render(request, 'edituser/changepassword.html')
    else:
	return index(request)

def passwordchanged(request):
    if request.user.is_authenticated():
	username = request.user.username
	passwordtest = request.POST.get('currentpassword')
	newpassword = request.POST.get('newpassword1')
	newpassword2 = request.POST.get('newpassword2')
	newuser = User.objects.get(username=username)
	user = authenticate(username = username, password = passwordtest)
	if user is not None:
	    if user.is_active:
		if newpassword == newpassword2:
		    newuser.set_password(newpassword)
		    newuser.save()
		    logout(request)
		    return index(request)
		else:
		    blob = newpassword + " : " + newpassword2
		    return HttpResponse("your new passwords don't match eachother, oh no")
	    else:
		return HttpResponse("that's odd.  it appears you aren't an active user")
	else:
	    return HttpResponse("I could not verify your password, please try again")
    else:
	return index(request)
