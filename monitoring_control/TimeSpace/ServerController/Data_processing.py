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

    def load_service_data_and_calulating(self, host_obj, trigger_obj, redis_obj):
        self.redis = redis_obj
        calc_sub_res_list = []
        positive_expressions = []
        expression_res_string = ''
        for expression in trigger_obj.triggerexpression_set.select_related().order_by('id'):
            print(expression,expression.logic_type)
            exprpession_process_obj = ExpressionProcess(self,host_obj, expression)
            single_expression_res = expression_process_obj.process()
            if single_expression_res:
                calc_sub_res_list.append(single_expression_res)
                if single_expression_res['expression_obj'].logic_type:
                    expression_res_string += str(single_expression_res['calc_res']) + ' ' + \
                                             single_expression_res['expression_obj'].logic_type + 







class ExpressionProcess(object):

    def __init__(self,):


    def process(self):
        data = self.load_data_from_redis()
        data_calc_func = getattr(self, 'get_%s' % self.expression_obj)
        single_expression_calc_res = data_calc_fun(data)
        print("--- res of single_expression_calc_res", single_expression_calc_res)
        if single_expression_calc_res:
            res_dic = {
                'calc_res': single_expression_calc_res[0],
                'calc_res_val': single_expression_calc_res[1],
                'expression_obj': self.expression_obj,
                'service_item': single_expression_calc_res[2],
            }



    def load_data_from_redis(self):
        time_in_sec = int(self.time_range) * 60
        approximate_data_points = (time_in_sec + 60) / self.expression_obj.service.interval
        print("approximate dataset nums:", approximate_data_points, time_in_sec)
        data_range_raw = self.main_ins.redis.lrange(self.service_redis_key, -approximate_data_points, -1)
        approximate_data_range = [json.loads(i) for i in data_range_raw]
        data_range = []
        for point in approximate_data_range:
            val, saving_time = point
            if time.time() - saving_time < time_in_sec:
                data_range.append(point)