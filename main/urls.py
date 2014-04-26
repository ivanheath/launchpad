from django.conf.urls.defaults import *
from main import views

urlpatterns = patterns('',
    url(r'^/', views.main, name='launchpad'),
)

