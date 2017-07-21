from django.db import models
from datetime import datetime
# Create your models here.
class UserInfo(models.Model):
    USER_ROLE_CHOICES = (
        (0, 'member'),
        (1, 'admin'),
        (2, 'superadmin'),
    )

    username = models.CharField(max_length=20, verbose_name=u"用户名")
    email = models.EmailField(verbose_name=u"邮箱")
    userpass = models.CharField(max_length=20, verbose_name=u"密码")
    image = models.ImageField(upload_to="image/%Y/%m", max_length=100, default=u"/static/images/default.jpg", verbose_name=u"图像")
    position = models.CharField(max_length=20, verbose_name=u"用户职位")
    user_type = models.IntegerField(choices=USER_ROLE_CHOICES, verbose_name=u"用户类型", null=False, default=0)

    class Meta:
        verbose_name = u"用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return ("<%s %s %s>" % (self.username, self.position, self.user_type))


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name=u"验证码")
    email = models.EmailField(max_length=20, verbose_name=u"邮箱")
    send_type = models.CharField(choices=(("register",u"注册"),("forget",u"找回密码")),max_length=10)
    send_time = models.DateTimeField(default=datetime.now())

    class Meta:
        verbose_name = u"邮箱验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return ("<%s>" % self.code)




















