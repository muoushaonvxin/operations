from django.db import models

# Create your models here.
class HostScan(models.Model):
    host = models.IPAddressField(max_length=32,verbose_name=u"主机地址")
    port = models.IntegerField(max_length=10, verbose_name=u"端口号")
