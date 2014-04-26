from django.conf.urls.defaults import *
from newsfeed import views

urlpatterns = patterns('',
    url(r'^newspost/', views.newspostform, name='postnews'),
    url(r'^postnews', views.posttonews, name='posttonews'),
    url(r'^message/', views.message, name='message'),
    url(r'^deletenewspost', views.delete, name='deletenewspost'),
    url(r'^newsdeleted', views.postdeleted, name='newsdeleted'),
)
