from django.db import models
from datetime import datetime
from host.models import host as des_host
# Create your models here.

class ssh_crack_detail(models.Model):
    host_ip = models.GenericIPAddressField(verbose_name=u"目标ip地址")
    username = models.CharField(max_length=50, verbose_name=u"用户名")
    password = models.CharField(max_length=50, verbose_name=u"破解的密码")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    host = models.ForeignKey(des_host)

    def __str__(self):
        return "<host ip address is %s, username is %s, password is %s>"


class ssh_crack_failed(models.Model):
    host_ip = models.GenericIPAddressField(verbose_name=u"目标ip地址")
    username = models.CharField(max_length=50, verbose_name=u"用户名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    host = models.ForeignKey(des_host)

    def __str__(self):
        return self.host_ip