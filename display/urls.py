# -*- coding: utf-8 -*-
__author__ = 'buzz'
__date__ = '2018/4/16 下午10:14'

from django.conf.urls import url

from . import views

app_name = 'display'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^chartstest/$', views.charts_test, name='charts_test'),
    url(r'^temperature/$', views.temp_display, name='charts_temp'),
    url(r'^pressure/$', views.pressure_display, name='charts_pres'),
    url(r'^gas/$', views.gas_display, name='charts_gas'),
    url(r'^alarm/$', views.alarm, name='alarm'),
    url(r'^logs/$', views.log, name='calendar_logs'),
]
