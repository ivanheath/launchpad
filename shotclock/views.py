from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
import urllib2
from django.core import serializers
from django.utils import simplejson
import json
import datetime
from maintenancetracker.models import maintenance

def clock(request):
    test = "loaded test"
    test2 = "test2"
    list = []
    response = urllib2.urlopen("http://omega.wowrack.com/ticketdash/app/dashboard/ajaxall")
    response = response.read()
    test2 = simplejson.loads(response)
    response = json.loads(response)
    response = response['data']
    for i in response:
	if i["company_id"] == '1':
	    company_id = 'wowrack'
	elif i["company_id"] == '2':
	    company_id = 'serverstadium'
	elif i["company_id"] == '3':
	    company_id = "wowindo"
	list.append(i["product_id"])
	list.append(company_id)
	x = datetime.datetime.now()
	y = datetime.datetime.fromtimestamp(int(i["approve_date"]))
	list.append(x.replace(second=0, microsecond=0) - y.replace(second=0, microsecond=0))
    
    currentmaintlist = maintenance.objects.filter().order_by('-maint_time')
    for i in currentmaintlist:
	timer = datetime.datetime.now() - datetime.timedelta(hours=1)
	if i.maint_time <= timer:
	    i.delete()
    return render(request, 'shotclock/shotclock.html',
	{"list": list,
	 "currentmaintlist": currentmaintlist,
	})
