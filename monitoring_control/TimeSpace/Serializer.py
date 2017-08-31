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
                host_obj_id = Host.objects.get(ip_addr=self.client_ip)
                print(">>>>>>>>", host_obj_id)
                template_list = list(host_obj_id.templates.select_related())
                print(">>>>>>>>", template_list)
                host_group_obj = host_obj_id.host_groups.select_related()
                template_list.extend([template for template in host_group_obj])
                print(">>>>>>>>", template_list)
                for template in template_list:
                    for service in template.services.select_related():
                        print(service)
                        self.client_configs['services'][service.name] = [service.plugin_name, service.interval]
            except Exception as e:
                print(u"没有这个客户端!")
        except:
            traceback.print_exc()
        print(self.client_configs)
        return self.client_configs