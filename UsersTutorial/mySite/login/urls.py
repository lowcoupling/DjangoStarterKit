'''
Created on 22/apr/2013

@author: lowcoupling
'''
from django.conf.urls import patterns, url

from login import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'login', views.login_view, name='login'),
    url(r'logout', views.logout_view, name = 'logout'),
)