from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from login.views import index
import subprocess

def main(request):
    if request.user.is_authenticated():
	username = request.user.username
	#test = subprocess.check_output("echo drivetool | ssh -t web@10.15.14.27 sudo -S -k ls", shell=True)
	return render(request, 'drivetool/main.html',
	    {"username":username,
	    })
    else:
	return index(request)

def scandrives(request):
    if request.user.is_authenticated():
	username = request.user.username
	harddrivelist = []
	remotepass = "echo drivetool | ssh web@10.15.14.27 sudo -S -k "
	for i in range(98, 122):
	    hddletter = chr(i)
	    hdd = subprocess.Popen(remotepass + "ls /sys/block | grep sd%s" %hddletter, shell=True, stdout=subprocess.PIPE)
	    hdd = hdd.stdout.read().strip()
	    if hdd != '':
		hddinfo = subprocess.check_output(remotepass + "smartctl -a /dev/%s" %hdd, shell=True).splitlines()
		hddmodel = hddinfo[5]
		hddmodel = "Model" + hddmodel[12:]
		hddserial = hddinfo[6]
		hddserial = "Serial" + hddserial[13:]
		hddhours = hddinfo[62]
		hddhours = hddhours[-11:].strip() + " hours on"
		hddsmart = hddinfo[19]
		hddsmart = hddsmart[-7:].strip()
		hddlocation = subprocess.Popen(remotepass + "file /sys/block/%s" %hdd, stdout=subprocess.PIPE, shell=True)
		hddlocation = hddlocation.stdout.read()[-20:-18].strip()
		hddlocation = locator(hddlocation)
		if hddsmart != 'PASSED':
		    hddsmart = 'FAILED SMART TEST'
		else:
		    hddsmart = 'PASSED SMART TEST'
		currenthdd = harddrive(hdd, hddmodel, hddserial, hddhours, hddsmart, hddlocation)
		harddrivelist.append(currenthdd)
		harddrivelist.sort(key=lambda x: x.location)
		harddrivelist = layoutbuilder(harddrivelist)
	return render(request, 'drivetool/drives.html',
		     {"hddlist": harddrivelist,
		      "username": username,
		     })
    else:
	return index(request)

def wipedrives(request):
    if request.user.is_authenticated():
        username = request.user.username
	hddlist = []
	remotepass = "echo drivetool | ssh web@10.15.14.27 sudo -S -k "
	wipestring = "dcfldd pattern=00 "
	for i in range(98, 122):
            hddletter = chr(i)
            hdd = subprocess.Popen(remotepass + "ls /sys/block | grep sd%s" %hddletter, stdout=subprocess.PIPE, shell=True)
            hdd = hdd.stdout.read().strip()
            if hdd != '':
                hddserial = subprocess.Popen(remotepass + "smartctl -a /dev/%s | grep 'Serial Number'" %hdd, stdout=subprocess.PIPE, shell=True)
                hddserial = hddserial.stdout.read()[14:].strip()
                if hddserial != 'WD-WCASYD980519':
                    wipestring = wipestring + "of=/dev/%s " %hdd
	#subprocess.call(remotepass + wipestring, shell=True)
	return render(request, 'drivetool/wipe.html',
		     {"username":username,
		     })
    else:
	return index(request)

def clonedrives(request):
    if request.user.is_authenticated():
	username=request.user.username
	hddlist = []
	goodmark = 0
	remotepass = "echo drivetool | ssh web@10.15.14.27 sudo -S -k "
	clonestring = "dcfldd if=/dev/"
	tobecloned = ""
	for i in range(98, 122):
            hddletter = chr(i)
            hdd = subprocess.Popen(remotepass + "ls /sys/block | grep sd%s" %hddletter, stdout=subprocess.PIPE, shell=True)
            hdd = hdd.stdout.read().strip()
            if hdd != '':
                hddlocation = subprocess.Popen(remotepass + "file /sys/block/%s" %hdd, stdout=subprocess.PIPE, shell=True)
                hddlocation = hddlocation.stdout.read()[-20:-18].strip()
                hddlocation = locator(hddlocation)
                if hddlocation == 1:
                    clonestring = clonestring + hdd
                    goodmark = 1
                else:
                    tobecloned = tobecloned + " of=/dev/" + hdd
        if goodmark == 0:
            return HttpResponse('no drive is loaded in slot one.  please load a drive in slot one to be cloned')
        elif tobecloned == "/":
            return HttpResponse("there are no drives to be cloned. this ain't gonna work")
        else:
            clonestring = clonestring + tobecloned + " &"
            #subprocess.call([clonestring], shell=True)
            return render(request, 'drivetool/clone.html',
			 {"username":username,
			 })
    else:
	return index(request)

def cleandrives(request):
    if request.user.is_authenticated():
        username = request.user.username
	remotepass = "echo drivetool | ssh web@10.15.14.27 sudo -S -k "
	for i in range(98, 122):
            hddletter = chr(i)
            hdd = subprocess.Popen(remotepass + "ls /sys/block | grep sd%s" %hddletter, stdout=subprocess.PIPE, shell=True)
            hdd = hdd.stdout.read().strip()
            if hdd != '':
                cleanstring = "dcfldd pattern=00 bs=512 count=1024 of=/dev/%s &" %hdd
                blockcount = subprocess.Popen(remotepass + "blockdev --getsz /dev/%s" %hdd, stdout=subprocess.PIPE, shell=True)
                blockcount = blockcount.stdout.read().strip()
                blockcount = int(blockcount)
                blockcount = blockcount - 2048
                raidstring = "dcfldd pattern=00 bs=512 count=2048 seek=%s of=/dev/%s &" %(blockcount, hdd)
                #subprocess.call(remotepass + cleanstring, shell=True)
                #subprocess.call(remotepass + raidstring, shell=True)
	return render(request, 'drivetool/clean.html',
		     {"username":username,
		     })
    else:
	return index(request)

def configure(request):
    if request.user.is_authenticated():
	username = request.user.username
	return render(request, 'drivetool/configure.html',
		     {"username":username,
		     })
    else:
	return index(request)


class harddrive:

    def __init__(self, sd, model, serial, hours, smart, location):
        self.sd = sd
        self.model = model
        self.serial = serial
        self.hours = hours
        self.smart = smart
        self.location = location


def hourstest(hddhours):
    try:
        a = int(hddhours)
    except:
        hddhours = 9999999999
    if int(hddhours) == 9999999999:
        hddhours = "EPIC FAIL"
    elif int(hddhours) > 35040:
        hddhours = str(hddhours) + " TOO OLD"
    elif int(hddhours) > 17520:
        hddhours = (hddhours) + " SS ONLY"
    return hddhours


def locator(location):

    if location == '12':
        location = 1
    elif location == '13':
        location = 2
    elif location == '14':
        location = 3
    elif location == '15':
        location = 4
    elif location == '/8':
        location = 5
    elif location == '/9':
        location = 6
    elif location == '10':
        location = 7
    elif location == '11':
        location = 8
    elif location == '/4':
        location = 9
    elif location == '/5':
        location = 10
    elif location == '/7':
        location = 11
    elif location == '/6':
        location = 12
    elif location == '/0':
        location = 13
    elif location == '/1':
        location = 14
    elif location == '/2':
        location = 15
    elif location == '/3':
        location = 16
    return location


def layoutbuilder(harddrivelist):
    hddlist = []
    currenthdd = harddrive('', '', 'EMPTY', '', '', 1)
    for x in range(1, 17):
        for y in harddrivelist:
            if y.location == x:
                currenthdd = y
                locationtest = 1
        if currenthdd.location != x:
            currenthdd = harddrive('', '', 'EMPTY', '', '', x)
        hddlist.append(currenthdd)

    return hddlist

