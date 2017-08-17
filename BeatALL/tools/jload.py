import re,json
from collections import OrderedDict

# 匹配ajax传递过来的json数据,并把json传递过来的数组进行排序 (需要结合checkbox来进行使用,适用于全部字符串的场景)
def jsonzh(data):
    data = json.loads(data, object_pairs_hook=OrderedDict)
    k1 = []
    v1 = []
    d1 = {}

    for k,v in data.items():
        if re.match('^\d+', v):
            k1.append(int(v))
        if not re.match('^\d+', v):
            v1.append(v)

    for index in range(len(k1)):
        d1[k1[index]] = v1[index]

    return d1


def jsonsingle(data):
    data = json.loads(data, object_pairs_hook=OrderedDict)
    l1 = []

    for v in data.values():
        l1.append(v)

    l1_length = len(l1)

    count = l1_length/4
