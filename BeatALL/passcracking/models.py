from django.db import models

# Create your models here.
class PasswordCrack(models.Model):
    pass


class ssh_crack(models.Model):
    host = models.GenericIPAddressField(verbose_name=u"目标ip地址")
    name = models.CharField(max_length=32, null=True, blank=True, verbose_name=u"目标命名")


class ssh_crack_detail(models.Model):
    password = models.CharField(max_length=50, verbose_name=u"破解的密码")
    ssh_crack = models.ForeignKey(ssh_crack)

    def __str__(self):
        return "<%s>" % self.password