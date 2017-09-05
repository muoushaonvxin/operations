import traceback
from django.views.generic import View
from TimeSpace.models import Host


class ClientHandler(View):

    def __init__(self, client_ip):
        self.client_ip = client_ip
        self.client_configs = {
            "services": {}
        }

    def fetch_configs(self):
        try:
            try:
                host_obj = Host.objects.get(ip_addr=self.client_ip)
                template_list = list(host_obj.templates.select_related())
                for host_group in host_obj.host_groups.select_related():
                    template_list.extend(host_group.templates.select_related())
                for template in template_list:
                    for service in template.services.select_related():
                        self.client_configs['services'][service.name] = [service.plugin_name, service.interval]
            except Exception as e:
                print(u"没有这个客户端!")
        except:
            traceback.print_exc()
        return self.client_configs


class GetTrigger(object):

    def __init__(self, host_obj):
        self.host_obj = host_obj
        self.trigger_configs = []

    def get_trigger(self):
        for template in self.host_obj.templates.select_related():
            self.trigger_configs.extend(template.triggers.select_related())
        for group in self.host_obj.host_groups.select_related():
            for template in group.templates.select_related():
                self.trigger_configs.extend(template.triggers.select_related())
        return set(self.trigger_configs)

    def load_service_data_and_calulating(self, host_obj, trigger, REDIS_OBJ):
        pass


