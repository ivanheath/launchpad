from django.conf.urls.defaults import *
from shotclock import views

urlpatterns = patterns('',
    url(r'^shotclock/', views.clock, name='shotclock')
)

