from django.db import models

# Create your models here.
class PasswordCrack(models.Model):
    pass


class ssh_crack(models.Model):
    host = models.GenericIPAddressField(verbose_name=u"目标ip地址")
    dictionary = models.CharField(max_length=32,verbose_name=u"字典名称")
    user = models.CharField(max_length=32, default="root" ,verbose_name=u"用户")
    name = models.CharField(max_length=32, null=True, blank=True, verbose_name=u"目标命名")

    def __str__(self):
    	return "<%s>" % self.host

class ssh_crack_detail(models.Model):
    password = models.CharField(max_length=50, verbose_name=u"破解的密码")
    ssh_crack = models.ForeignKey(ssh_crack)

    def __str__(self):
        return "<%s>" % self.password