from django.shortcuts import render, HttpResponse
from tools.ssh_connect import ssh_connect
from passcracking import models
import json
from passcracking import forms
from tools.jload import jsonzh, jsonsingle
import django.utils.timezone as timezone
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime

# Create your views here.



def ssh_crack(request):
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1
    ssh_obj = models.ssh_crack.objects.all()
    p = Paginator(ssh_obj, 5, request=request)
    ssh_record = p.page(page)
    return render(request, 'host/ssh_crack.html', {
        'ssh_record': ssh_record,
        'ssh_obj': ssh_obj,
    })


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
