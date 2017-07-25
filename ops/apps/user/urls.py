# -*- encoding: utf-8 -*-
__author__ = "zhangyz"
__date__ = "2017/6/19 22:41"

from django.conf.urls import url
from user import views

urlpatterns = [
    url(r'alterPasswd/$', views.alterPasswd),
]