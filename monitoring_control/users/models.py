from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name=u"名称", default="")
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name=u"电话号码")
    image = models.ImageField(upload_to="image/%Y/%m", default=u"image/default.png", max_length=100, verbose_name=u"个人图像")
    type = models.IntegerField(default=0, verbose_name=u"用户类型", choices=((0, u"普通用户"), (1, u"管理员")))
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name=u"验证码")
    email = models.EmailField(max_length=50, verbose_name=u"邮箱")
    send_type = models.CharField(verbose_name=u"验证码类型", max_length=30)
    send_time = models.DateTimeField(verbose_name=u"发送时间", default=datetime.now)

    class Meta:
        verbose_name = u"邮箱验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0},({1})'.format(self.code, self.email)


class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name=u"标题")
    image = models.ImageField(upload_to="banner/%Y/%m", verbose_name=u"轮播图", max_length=100)
    url = models.URLField(max_length=200, verbose_name=u"访问地址")
    index = models.IntegerField(default=100, verbose_name=u"顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"轮播图"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
























