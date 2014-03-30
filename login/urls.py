from django.conf.urls import patterns, url
from login import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^main/', views.authenticater, name='main'),
    url(r'^logout/', views.logout_now, name='logout'),
)

