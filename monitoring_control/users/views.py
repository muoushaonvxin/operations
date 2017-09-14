from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import UserProfile, Banner
from django.views import View
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
# Create your views here.


class LoginView(View):
    """
        用户登录
    """
    def get(self, request):
        return render(request, "login.html", {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse("index"))
                else:
                    return render(request, "login.html", {"msg":u"用户未激活!"})
            else:
                return render(request, "login.html", {"msg":u"用户名或密码错误!"})
        else:
            return render(request, "login.html", {"login_form":login_form})


class LogoutView(View):
    """
        用户登出
    """
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse("login"))


class IndexView(View):
    def get(self, request):
        all_banners = Banner.objects.all().order_by('index')
        return render(request, "index.html", {
            'all_banner': all_banners,
        })


