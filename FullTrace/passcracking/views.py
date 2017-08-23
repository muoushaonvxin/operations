from django.shortcuts import render, HttpResponse
from tools.ssh.ssh_connect import ssh_connect
from passcracking import models
import json
from tools.ssh.jload import jsonzh, json_ssh_crack_passwd
from django.views import View
from host.models import host as hostlist

# Create your views here.

class dos_ssh_user_password_view(View):
    def post(self, request):
        ssh_data = json_ssh_crack_passwd(request.POST.get("jsonstr", ""))
        for data in ssh_data:
            print(data)
            ssh_value = ssh_connect(data[1], int(data[2]), data[3], data[4])
            ssh_value_success = ssh_value['ssh_value_success']
            if len(ssh_value_success) == 0:
                models.ssh_crack_failed(host_ip=hostlist.objects.get(id=int(data[0])).host_ip,username=data[4],
                                        host=hostlist.objects.get(id=int(data[0]))).save()
                print("没有找到正确的密码!")
            elif ssh_value_success[0] == 1:
                models.ssh_crack_detail(host_ip=hostlist.objects.get(id=int(data[0])).host_ip,username=data[4],password=ssh_value_success[1],
                                        host=hostlist.objects.get(id=int(data[0]))).save()
                print("密码找到,添加成功!")
        msg = u"主机破解结束"
        return HttpResponse(json.dumps({"jsonstr":msg}), content_type="application/json")







