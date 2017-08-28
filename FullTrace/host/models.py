from django.db import models
from datetime import datetime

# Create your models here.
class host(models.Model):
    host_ip = models.GenericIPAddressField(verbose_name=u"目标ip地址")
    port = models.IntegerField(verbose_name=u"端口")
    dictionary = models.CharField(max_length=32,verbose_name=u"字典名称")
    user = models.CharField(max_length=32, default="root" ,verbose_name=u"用户")
    name = models.CharField(max_length=32, null=True, blank=True, verbose_name=u"目标命名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    def __str__(self):
        return "<%s>" % self.host_ip


