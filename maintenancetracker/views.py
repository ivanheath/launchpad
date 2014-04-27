from django.http import HttpResponse
from django.shortcuts import render
import datetime
from maintenancetracker.models import maintenance
from login.views import index
from main.views import main as homepage
from forms import maintform
from forms import deleteform
from maintenancetracker.models import maintenance

def mainttracker(request):
    #currentmaintlist = maintenance.objects.filter().order_by('-maint_time')
    #for i in currentmaintlist:
	#if i.maint_time <= datetime.datetime.now():
	    #i.delete()
    return render(request, 'maintenancetracker/maintenancetracker.html', {"currentmaintlist":currentmaintlist})

def create(request):
   if request.user.is_authenticated():
	username = request.user.username
	if request.method == 'POST':
	    form = maintform(request.POST)
	    if form.is_valid():
		addmaint = form.cleaned_data
		maint = maintenance(maint_name=addmaint['maintname'], maint_time=addmaint['mainttime'], ticket_number=addmaint['maintticket'], ticket_link=addmaint['maintlink'], company=addmaint['maintcompany'])
		maint.save()
		return homepage(request)
	else:
	    form = maintform()
	return render(request, 'maintenancetracker/createmaintenance.html', {'form':form, 'username': username})
   else:
	return index(request)



def delete(request):
    if request.user.is_authenticated():
	username = request.user.username
	if request.method == 'POST':
	    form = deleteform(request.POST)
	    if form.is_valid():
		deletemaint = form.cleaned_data
		deletemaintenance = maintenance.objects.filter(maint_name=deletemaint['maintdel'])
		#maint = maintenance.objects.filter(maint_name=deletemaint['maintname', mainttime=deletemaint['mainttime'])
		deletemaintenance.delete()
		return homepage(request)
	else:
	    form = deleteform()
        return render(request, "maintenancetracker/deletemaintenance.html", {'form':form, 'username': username})
    else:
	return index(request)

def edit(request):
    return HttpResponse("edit")


