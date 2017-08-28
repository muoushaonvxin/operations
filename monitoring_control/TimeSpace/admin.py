from django.contrib import admin
from .models import Host, HostGroup, ServiceIndex, Service
from .models import Template, Trigger, TriggerExpression, Action, ActionOperation, Maintenance, EventLog


# Register your models here.
class HostAdmin(admin.ModelAdmin):
    list_display = ('id', 'ip_addr', 'status')
    filter_horizontal = ('host_groups', 'templates')


class TemplateAdmin(admin.ModelAdmin):
    filter_horizontal = ('services', 'triggers')


class ServiceAdmin(admin.ModelAdmin):
    filter_horizontal = ('items', )
    list_display = ('name', 'interval', 'plugin_name')


class TriggerExpressionInline(admin.ModelAdmin):
    model = TriggerExpression


class TriggerAdmin(admin.ModelAdmin):
    list_display = ('name', 'serverity', 'enabled')
    inlines = [TriggerExpressionInline]


class TriggerExpressionAdmin(admin.ModelAdmin):
    list_display = ('trigger', 'service', 'service_index', 'specified_index_key')



admin.site.register(Host, HostAdmin)
admin.site.register(HostGroup)
admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceIndex)
admin.site.register(Template, TemplateAdmin)
admin.site.register(Trigger, TriggerAdmin)
admin.site.register(TriggerExpression, TriggerExpressionAdmin)
admin.site.register(Action)
admin.site.register(ActionOperation)
admin.site.register(Maintenance)
admin.site.register(EventLog)

