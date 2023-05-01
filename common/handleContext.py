# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: handleContext.py
# @Author: Luke
# @Time: 3月 31, 2023


import re
import random
import datetime
from common import conFig


startDay = str(datetime.date.today())


class Context:
    # login
    unionid = conFig.getValue('LoginInfo', 'unionid')

    # general
    amount = str(round(random.uniform(4, 100), 2))

    p = "\$\{(.*?)}"

    def replace(self, s, d):
        while re.search(self.p, s):
            m = re.search(self.p, s)
            key = m.group(1)
            value = d[key]
            s = re.sub(self.p, value, s, count=1)
        return s

    def replace_new(self, s):
        while re.search(self.p, s):
            m = re.search(self.p, s)
            key = m.group(1)
            if hasattr(Context, key):
                value = getattr(Context, key)
                s = re.sub(self.p, value, s, count=1)
            else:
                print("没有这个属性值")
                return None
        return s

    def replace_list(self, s):
        new_data_list = list(filter(lambda x: re.match(self.p, x) != None, s))
        return new_data_list


if __name__ == '__main__':
    pass
