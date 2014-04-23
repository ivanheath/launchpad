from django.conf.urls import patterns, url, include
from maintenancetracker import views

urlpatterns = patterns('',
    url(r'^maintenancetracker/create', views.create, name='maintcreate'),
    url(r'^maintenancetracker/created', views.created, name='maintcreated'),
    url(r'^maintenancetracker/delete', views.delete, name='maintdelete'),
    url(r'^maintenancetracker/edit', views.edit, name='maintedit'),
    url(r'^maintenancetracker/', views.mainttracker, name='mainttrack'),
)
