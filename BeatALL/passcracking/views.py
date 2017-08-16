from django.shortcuts import render, HttpResponse
from tools.ssh_connect import ssh_connect
from passcracking import models
import json
from passcracking import forms

# Create your views here.
def ssh_crack(request):
    form = forms.ssh_crack_ModelForm()
    if request.method == "POST":
        print(request.POST)
        form = forms.ssh_crack_ModelForm(request.POST)
        if form.is_valid():
            print("form is ok!")
            print(form)
            print(form.cleaned_data)
            form.save()
        else:
            print(form.errors)
    ssh_obj = models.ssh_crack.objects.all()
    return render(request, 'ssh_crack.html', {'ssh_obj': ssh_obj,
                                              'ssh_form': form})


def dos_ssh_root_password(request):
    form = forms.ssh_crack_ModelForm()
    if request.method == "POST":
        form = forms.ssh_crack_ModelForm(request.POST)
        if form.is_valid():
            ssh_value = ssh_connect(request.POST.get('hostname', ''), int(request.POST.get('port', '')),
                                    request.POST.get('dictionary', ''), request.POST.get('username', ''))
            if ssh_value[0] == 1:
                s = ssh_crack(host=request.POST.get('hostname', ''),
                              port=int(request.POST.get('port', ''),
                              dictionary=request.POST.get('dictionary', '')),
                              user=request.POST.get('user', ''),
                              name=request.POST.get('name', ''))
                s.save()

                s_obj = ssh_crack.objects.all().last()
                models.ssh_crack_detail(password=ssh_value[1], ssh_crack=s_obj)
                return HttpResponse()
    return HttpResponse(u'没有执行成功!')
