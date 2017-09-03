import time, threading, json
import requests
from conf import settings
from plugins import plugin_api


class ClientHandlers(object):

    def __init__(self):
        self.monitor_services = {}


    def load_latest_config(self):
        """
        加载最新的配置信息
        :return:
        """
        request_type = settings.configs["urls"]["get_configs"][1]
        request_url = "%s/%s" % (settings.configs["urls"]["get_configs"][0], settings.configs["HostIP"])
        lastest_config = self.url_request(request_type, request_url)
        self.monitor_services.update(lastest_config)


    def forever_run(self):
        exit_flag = False
        config_lastest_update_time = 0
        while not exit_flag:
            if time.time() - config_lastest_update_time > settings.configs["ConfigUpdateInterval"]:
                self.load_latest_config()
                print("Lastest_config:", self.monitor_services)
                config_lastest_update_time = time.time()

            for service_name, val in self.monitor_services["services"].items():
                if len(val) == 2:
                    self.monitor_services["services"][service_name].append(0)
                monitor_interval = val[1]
                last_invoke_time = val[2]
                if time.time() - last_invoke_time > monitor_interval:
                    print("---->", last_invoke_time, "---->", time.time())
                    self.monitor_services["services"][service_name][2] = time.time()
                    t = threading.Thread(target=self.invoke_plugin, args=(service_name, val))
                    t.start()
                    print("start monitor service: [{ServiceName}]".format(ServiceName=service_name))
                else:
                    print("Going to monitor service [{ServiceName}] in [{interval}] secs".format(ServiceName=service_name, interval=monitor_interval - (time.time() - last_invoke_time)))
                    time.sleep(1)


    def invoke_plugin(self, service_name, val):
        plugin_name = val[0]
        if hasattr(plugin_api, plugin_name):
            func = getattr(plugin_api, plugin_name)
            plugin_callback = func()
            print(plugin_callback)

            report_data = {
                "client_ip": settings.configs['HostIP'],
                "service_name": service_name,
                "data": json.dumps(plugin_callback),
            }

            request_action = settings.configs["urls"]["service_report"][1]
            request_url = settings.configs["urls"]["service_report"][0]
            self.url_request(request_action, request_url, params=report_data)
        else:
            print("\033[31mCannot find service [%s]' plugin name [%s] in plugin_api\033[0m" % (service_name, plugin_name))
        print('--plugin:', val)


    def url_request(self, action, request_url, **extra_data):
        abs_url = "http://{ip_addr}:{port}/{url}".format(ip_addr=settings.configs["Server"],
                                                         port=settings.configs["ServerPort"],
                                                         url=request_url)
        print("\033[31m{abs_url}\033[0m".format(abs_url=abs_url), type(extra_data), extra_data)
        print(extra_data)
        if action in ('get', "GET"):
            print(abs_url, extra_data)
            try:
                r = requests.get(abs_url, timeout=settings.configs["RequestTimeout"])
                r_data = r.json()
                return r_data
            except requests.RequestException as E:
                exit("\033[31;1m%s\033[0m" % E)

        elif action in ('post', 'POST'):
            try:
                data = json.dumps(extra_data['params'])
                req = requests.post(url=abs_url, data=extra_data["params"])
                res_data = req.json()
                print("------------------------------------------------------")
                print("\033[31;1m[%s]:[%s]\033[0m response:\n%s,%s" % (action, abs_url, res_data, data))
                print("------------------------------------------------------")
                return res_data
            except Exception as e:
                print('-----exce', e)
                print("\033[31m;1m%s\033[0m" % e)

























