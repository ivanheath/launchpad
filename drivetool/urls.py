from django.conf.urls.defaults import *
from drivetool import views

urlpatterns = patterns('',
    #url(r'^drivetool/drives', views.scandrives, name='scandrive'),
    url(r'^drivetool/wipeverify', views.wipeverify, name='wipeverify'),
    url(r'^drivetool/cleanverify', views.cleanverify, name='cleanverify'),
    url(r'^drivetool/cloneverify', views.cloneverify, name='cloneverify'),
    url(r'^drivetool/wipe', views.wipedrives, name='wipedrives'),
    url(r'^drivetool/clean', views.cleandrives, name='cleandrives'),
    url(r'^drivetool/clone', views.clonedrives, name='clonedrives'),
    url(r'^drivetool/configure', views.configure, name='configure'),
    url(r'^drivetool/main', views.scandrives, name='scandrives'),
    url(r'^drivetool/checkstatus', views.checkstatus, name='checkstatus'),
    url(r'^drivetool/', views.check, name='drivetool'),
    #url(r'^drivetool/drives', views.scandrives, name='scandrive'),
)
