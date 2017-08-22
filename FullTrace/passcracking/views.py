from django.shortcuts import render, HttpResponse
from tools.ssh_connect import ssh_connect
from passcracking import models
import json
from tools.jload import jsonzh, jsonsingle
from datetime import datetime
from django.views import View
from host.models import host as hostlist

# Create your views here.

class dos_ssh_user_password_view(View):
    def post(self, request):
        data = jsonsingle(request.POST.get("jsonstr", ""))
        print(data)
        ssh_value = ssh_connect(data[1], int(data[2]), data[3], data[4])
        print(ssh_value)
        ssh_value_success = ssh_value['ssh_value_success']

        if len(ssh_value_success) == 0:
            msg = u"没有执行成功!"
            return HttpResponse(json.dumps({"jsonstr": msg}), content_type='application/json')

        elif ssh_value_success[0] == 1:
            models.ssh_crack_detail(host_ip=hostlist.objects.get(id=int(data[0])).host_ip,
                                    username=data[4],
                                    password=ssh_value_success[1],
                                    add_time=datetime.now(),
                                    host=hostlist.objects.get(id=int(data[0]))).save()
            msg = u"添加成功!"
            return HttpResponse(json.dumps({"jsonstr": msg}), content_type='application/json')











