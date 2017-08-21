from django.db import models
from datetime import datetime
from host.models import host as des_host
# Create your models here.


class PasswordCrack(models.Model):
    pass


class ssh_crack_detail(models.Model):
    host = models.GenericIPAddressField(verbose_name=u"目标ip地址")
    password = models.CharField(max_length=50, verbose_name=u"破解的密码")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    host = models.ForeignKey(des_host)

    def __str__(self):
        return "<%s>" % self.password
