# -*- encoding: utf-8 -*-
import time
from .Redis_conn import redis_conn

class DataHandler(object):

    def __init__(self, django_settings, connect_redis=True):
        self.django_settings = django_settings
        self.poll_interval = 0,5
        self.config_update_interval = 120
        self.config_last_loading_time = time.time()
        self.global_monitor_dic = {}
        self.exit_flag = False
        if connect_redis:
            self.redis = redis_conn(self.django_settings)


    def looping(self):
        self.update_or_load_configs()
        count = 0
        while not self.exit_flag:
            print("looping %s".center(50,'-') % count)
            count += 1
            if time.time() - self.config_last_loading_time >= self.config_update_interval:
                print("\033[41;1mneed updaate configs ...\033[0m")
                self.update_or_load_configs()

            if self.global_monitor_dic:
                for h, config_dic in self.global_monitor_dic.items():
                    print("handling host:\033[32;1m%s\033[0m" % h)
                    for service_id, val in config_dic['services'].items():
                        service_obj, last_monitor_time = val
                        if time.time() - last_monitor_time >= service_obj.interval:
                            print("\033[33;1mservice [%s] has reached the monitor interval... \033[0m" % service_obj.name)
                            self.global_monitor_dic[h]['services'][service_obj.id][1] = time.time()
                            self.data_point_validation(h, service_obj)
                        else:
                            pass



    def update_or_load_configs(self):
        pass


    def data_point_validation(self):
        pass










