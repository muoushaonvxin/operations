from django.shortcuts import render, HttpResponse
from django.views.generic import View
import json
# Create your views here.

from monitor_client.Serializer import ClientHandler


class Client_Config_View(View):

    def get(self, request, client_id):
        client_obj = ClientHandler(client_id)
        client_config = client_obj.fetch_configs()
        print("客户端ID", client_id)
        if client_config:
            return HttpResponse(json.dumps(client_config), content_type="application/json")


class Service_Data_Report(View):
    def post(self, request):
        print(request.POST)
        try:
            print('host=%s, service=%s' % (request.POST.get('client_id'), request.POST.get('service_name')))
            data = json.loads(request.POST['data'])
            client_id = request.POST.get('client_id')
            service_name = request.POST.get('service_name')
            data_save_obj = data_optimization.DataStore(client_id, service_name, data, REDIS_OBJ)















