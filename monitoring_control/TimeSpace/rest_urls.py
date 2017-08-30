# -*- encoding: utf-8 -*-
from django.conf.urls import url, include
from .views import Client_Config_View

urlpatterns = [
    url(r'client/config/(\d+)/$', Client_Config_View.as_view()),
    # url(r'client/service/report/$', Service_Data_Report),
]