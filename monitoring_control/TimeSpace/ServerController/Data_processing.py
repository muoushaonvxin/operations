# -*- encoding: utf-8 -*-
import time
from .Redis_conn import redis_conn
import json

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
                                             single_expression_res['expression_obj'].logic_type + ' '
                else:
                    expression_res_string += str(single_expression_res['calc_res']) + ' '

                if single_expression_res['calc_res'] == True:
                    single_expression_res['expression_obj'] = single_expression_res['expression_obj']
                    positive_expressions.append(single_expression_res)
                    





class ExpressionProcess(object):

    def __init__(self, main_ins, host_obj, expression_obj, specified_item):
        self.host_obj = host_obj
        self.expression_obj = expression_obj
        self.main_ins = main_ins
        self.service_redis_key = "StatusData_%s_%s_latest" % (host_obj.ip_addr, expression_obj.service.name)
        self.time_range = self.expression_obj.data_calc_args.split(',')[0]
        print("\033[1m ------------> %s\033[0m" % self.service_redis_key)


    def process(self):
        data = self.load_data_from_redis()
        data_calc_func = getattr(self, 'get_%s' % self.expression_obj.data_calc_func)
        single_expression_calc_res = data_calc_fun(data)
        print("--- res of single_expression_calc_res", single_expression_calc_res)
        if single_expression_calc_res:
            res_dic = {
                'calc_res': single_expression_calc_res[0],
                'calc_res_val': single_expression_calc_res[1],
                'expression_obj': self.expression_obj,
                'service_item': single_expression_calc_res[2],
            }

            print("\033[41;1mmsingle_expression_calc_res: %s\033[0m" % )
            return res_dic
        else:
            return False



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

        print(data_range)
        return data_range



    def get_avg(self, data_set):

        clean_data_list = []
        clean_data_dic = {}
        for point in data_set:
            val, save_time = point

            if val:
                if 'data' not in val:
                    clean_data_list.append(val[self.expression_obj.service_index.key])
                else:
                    for k, v in val['data'].items():
                        if k not in clean_data_dic:
                            clean_data_dic[k] = []
                        clean_data_dic[k].append(v[self.expression_obj.service_index.key])

        if clean_data_list:
            clean_data_list = [float(i) for i in clean_data_list]
            avg_res = sum(clean_data_list) / len(clean_data_list)
            print("\033[46;1m ----- avg res: %s\033[0m" % avg_res)
            return [self.judge(avg_res), avg_res, None]
            print("clean_data_list: ", clean_data_list)
        elif clean_data_dic:
            for k, v in clean_data_dic.items():
                clean_v_list = [float(i) for i in v]
                avg_res = 0 if sum(clean_v_list) == 0 else sum(clean_v_list)
                print("\033[46;1m --%s--------avg res: %s\033[0m" % (k, avg_res))
                if self.expression_obj.specified_index_key:
                    if k == self.expression_obj.specified_index_key:





    def judge(self, calculated_val):
        calc_func = getattr(operator, self.expression_obj.operator_type)
        return calc_func(calculated_val, self.expression_obj.threshold)


    def get_hit(self, data_set):

















