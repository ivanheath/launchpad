from django.conf.urls import patterns, url, include
from shotclock import views

urlpatterns = patterns('',
    url(r'^shotclock/', views.clock, name='shotclock')
)

