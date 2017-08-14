from django.shortcuts import render
from tools.ssh_connect import ssh_connect
from passcracking.models import *

# Create your views here.
def dos_ssh_root_password(request):
    if request.method == "POST":
        ssh_connect(request.POST.get('hostname', ''), int(request.POST.get('port', '')),
                    request.POST.get('username', ''), request.POST.get('password', ''))
        if request.POST.get('hostname', '') is not None and  request.POST.get('port', '') is not None and request.POST.get('username', '') is not None and request.POST.get('password', '') is not None:
            ssh_crack(host=request.POST.get('hostname', ''), port=int(request.POST.get('port', ''))
