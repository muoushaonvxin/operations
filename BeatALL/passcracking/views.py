from django.shortcuts import render, HttpResponse
from tools.ssh_connect import ssh_connect
from passcracking import models
import json
from passcracking import forms
from tools.jload import jsonzh, jsonsingle

# Create your views here.
def add_crack(request):
    form = forms.ssh_crack_ModelForm()
    if request.method == "POST":
        print(request.POST)
        form = forms.ssh_crack_ModelForm(request.POST)
        if form.is_valid():
            print("form is ok!")
            print(form)
            print(form.cleaned_data)
            form.save()
            ssh_obj = models.ssh_crack.objects.all()
            return render(request, 'crack/ssh_crack.html', {'ssh_obj': ssh_obj})
        else:
            print(form.errors)
    return render(request, 'crack/add_crack.html', {'ssh_form': form})


def ssh_crack(request):
    ssh_obj = models.ssh_crack.objects.all()
    return render(request, 'crack/ssh_crack.html', {'ssh_obj': ssh_obj})


def dos_ssh_user_password(request):
    if request.method == "POST":
        data = jsonsingle(request.POST.get("jsonstr", ""))
        print(data)
    return HttpResponse(u'没有执行成功!')
