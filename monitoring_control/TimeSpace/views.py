from django.shortcuts import render, HttpResponse
from django.views.generic import View
import json
# Create your views here.

from monitor_client.Serializer import ClientHandler


class client_config_view(View):

    def get(self, request, client_id):
        client_obj = ClientHandler(client_id)
        client_config = client_obj.fetch_configs()
        print("客户端ID", client_id)
        if client_config:
            return HttpResponse(json.dumps(client_config), content_type="application/json")