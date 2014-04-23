from django.conf.urls import patterns, url
from edituser import views

urlpatterns = patterns('',
    url(r'^edituser/changed', views.savechanges, name="savechanges"),
    url(r'^edituser/passwordchanged', views.passwordchanged, name="passwordchanged"),
    url(r'^edituser/password', views.changepassword, name="changepassword"),
    url(r'^edituser/', views.main, name="edituser"),
)
