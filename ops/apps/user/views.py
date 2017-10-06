from django.shortcuts import render, HttpResponse
from user import models

# Create your views here.
def index(request):
    return render(request, "control.html")


def login(request):
    user_list = models.UserInfo.objects.all()
    if request.method == "POST":
        for user in user_list:
            if user.username == request.POST.get("username", "") and \
                            user.userpass == request.POST.get("password",""):
                return render(request, "main.html")
    msg = "用户名或密码错误"
    return render(request, "control.html", { 'error_msg': msg })


def addUser(request):
    if request.method == "POST":
        user = models.UserInfo(username=request.POST.get("username", ""),
                               email=request.POST.get("email",""),
                               userpass=request.POST.get("userpass",""),
                               position=request.POST.get("position",""),
                               user_type=request.POST.get("user_type",""))
        user.save()


def alterPasswd(request):
    userList = models.UserInfo.objects.all()
    for user in userList: print(user.userpass)
    oldPasswd = request.POST.get("oldPasswd", "")
    newPasswd = request.POST.get("newPasswd", "")
    print(oldPasswd, newPasswd)
    return render(request, 'user/alterPasswd.html')

