from django.shortcuts import render, HttpResponse
from tools.ssh_connect import ssh_connect
from passcracking import models
import json
from tools.jload import jsonzh, jsonsingle
from datetime import datetime

# Create your views here.

def dos_ssh_user_password(request):
    if request.method == "POST":
        data = jsonsingle(request.POST.get("jsonstr", ""))
        ssh_value = ssh_connect(data[1], int(data[2]), data[3], data[4])
        ssh_value_success = ssh_value['ssh_value_success']
        if ssh_value_success[0] == 1:
            models.ssh_crack_detail(host=models.ssh_crack.objects.get(host=data[1]).host,
                                    password=ssh_value_success[1],
                                    add_time=datetime.now(),
                                    ssh_crack=models.ssh_crack.objects.get(id=int(data[0]))).save()
            msg = u"添加成功"
            return HttpResponse(json.dumps({"jsonstr": msg}),
                                content_type='application/json')
    return HttpResponse(u'没有执行成功!')
