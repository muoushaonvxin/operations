from django.contrib import admin
from .models import Host, HostGroup, ServiceIndex, Service
from .models import Template, Trigger, TriggerExpression, Action, ActionOperation, Maintenance, EventLog


# Register your models here.
class HostAdmin(object):
    pass



admin.site.register(Host)
admin.site.register(HostGroup)
admin.site.register(Service)
admin.site.register(ServiceIndex)
admin.site.register(Template)
admin.site.register(Trigger)
admin.site.register(TriggerExpression)
admin.site.register(Action)
admin.site.register(ActionOperation)
admin.site.register(Maintenance)
admin.site.register(EventLog)

