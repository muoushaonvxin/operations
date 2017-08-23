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


# 用于给ssh密码取值, ssh密码五个值为一组
def json_ssh_crack_passwd(data):
    data = json.loads(data, object_pairs_hook=OrderedDict)
    l1 = []
    d1 = OrderedDict()  # 赋值一个OrderedDict字典

    for v in data.values():
        l1.append(v)

    x = len(l1)/5
    y = 0
    for i in range(0, int(x)):
        var1 = "v" + str(i)
        d1[var1] = []
        var2 = d1[var1]

        for j in [l1[j] for j in range(y, y + 5)]:
            var2.append(j)
        y+=5

    l2 = []
    for v in d1.values():
        l2.append(v)

    return l2