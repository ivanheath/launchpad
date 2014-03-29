from django.conf.urls import patterns, url
from main import views

urlpatterns = patterns('',
    url(r'^/main/', views.main, name='launchpad'),
)

