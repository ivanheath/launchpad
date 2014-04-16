from django.conf.urls import patterns, url, include
from drivetool import views

urlpatterns = patterns('',
    #url(r'^drivetool/drives', views.scandrives, name='scandrive'),
    url(r'^drivetool/wipe', views.wipedrives, name='wipedrives'),
    url(r'^drivetool/clean', views.cleandrives, name='cleandrives'),
    url(r'^drivetool/clone', views.clonedrives, name='clonedrives'),
    url(r'^drivetool/configure', views.configure, name='configure'),
    url(r'^drivetool', views.scandrives, name='drivetool'),
    #url(r'^drivetool/drives', views.scandrives, name='scandrive'),
)
