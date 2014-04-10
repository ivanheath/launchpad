from django.conf.urls import patterns, url
from newsfeed import views

urlpatterns = patterns('',
    url(r'^newspost/', views.newspostform, name='postnews'),
    url(r'^postnews', views.posttonews, name='posttonews'),
)
