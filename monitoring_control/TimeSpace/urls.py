from django.conf.urls import url, include
from .views import Client_Config_View
from TimeSpace import rest_urls

urlpatterns = [
    url(r'api/', include(rest_urls), name="api"),
]