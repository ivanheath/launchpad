from django.http import HttpResponse
from django.shortcuts import render
import datetime
from maintenancetracker.models import maintenance
from login.views import index
from main.views import main as homepage
from forms import maintform
from maintenancetracker.models import maintenance

def mainttracker(request):
    currentmaintlist = maintenance.objects.filter().order_by('-maint_time')
    for i in currentmaintlist:
	if i.maint_time <= timezone.now():
	    #i.delete()
	    plip = 4
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
    return render(request, "maintenancetracker/deletemaintenance.html")

def edit(request):
    return HttpResponse("edit")

def created(request):
    if request.user.is_authenticated():
	maintname = request.POST.get('maintname')
	mainttime = request.POST.get('mainttime')
	ticketnumber = request.POST.get('maintticket')
	ticketlink = request.POST.get('maintlink')
	company = request.POST.get('maintcompany')
	addmaint = maintenance(maint_name=maintname, maint_time=mainttime, ticket_number=ticketnumber, ticket_link=ticketlink, company=company)
	addmaint.save()
	return homepage(request)
    else:
	return index(request)
