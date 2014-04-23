from django.http import HttpResponse
from django.shortcuts import render
import datetime
from maintenancetracker.models import maintenance
from login.views import index
from main.views import main as homepage

def mainttracker(request):
    return render(request, 'maintenancetracker/maintenancetracker.html')

def create(request):
    return render(request, 'maintenancetracker/createmaintenance.html')

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
