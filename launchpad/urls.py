from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'launchpad.views.home', name='home'),
    # url(r'^launchpad/', include('launchpad.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('edituser.urls')),
    url(r'^', include('main.urls')),
    url(r'^', include('newsfeed.urls')),
    url(r'^', include('drivetool.urls')),
    url(r'^', include('login.urls')),
    url(r'^', include('shotclock.urls')),
    url(r'^', include('maintenancetracker.urls')),
)
