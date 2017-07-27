from django.db import models

# Create your models here.
class HostScan(models.Model):
    host = models.GenericIPAddressField(verbose_name=u"主机地址")
    port = models.IntegerField(verbose_name=u"端口号")
    add_time = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.host


class HostDetail(models.Model):
    host_ip = models.GenericIPAddressField(verbose_name=u"主机ip")
    host_details = models.CharField(max_length=255, verbose_name=u"主机详情")

    def __str__(self):
        return self.host_ip

