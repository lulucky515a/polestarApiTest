# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: identity.py
# @Author: Luke
# @Time: 4月 23, 2022


import random
import re
from datetime import datetime, timedelta
import common.identity.constant as const


class IdNumber(str):

    def __init__(self, id_number):
        super(IdNumber, self).__init__()
        self.id = id_number
        self.area_id = int(self.id[0:6])
        self.birth_year = int(self.id[6:10])
        self.birth_month = int(self.id[10:12])
        self.birth_day = int(self.id[12:14])

    def get_area_name(self):
        """根据区域编号取出区域名称"""
        return const.AREA_INFO[self.area_id]

    def get_birthday(self):
        """通过身份证号获取出生日期"""
        return "{0}-{1}-{2}".format(self.birth_year, self.birth_month, self.birth_day)

    def get_age(self):
        """通过身份证号获取年龄"""
        now = (datetime.now() + timedelta(days=1))
        year, month, day = now.year, now.month, now.day

        if year == self.birth_year:
            return 0
        else:
            if self.birth_month > month or (self.birth_month == month and self.birth_day > day):
                return year - self.birth_year - 1
            else:
                return year - self.birth_year

    def get_sex(self):
        """通过身份证号获取性别， 女生：0，男生：1"""
        return "male" if int(self.id[16:17]) % 2 == 1 else "female"

    def get_check_digit(self):
        """通过身份证号获取校验码"""
        check_sum = 0
        for i in range(0, 17):
            check_sum += ((1 << (17 - i)) % 11) * int(self.id[i])
        check_digit = (12 - (check_sum % 11)) % 11
        return check_digit if check_digit < 10 else 'X'

    @classmethod
    def verify_id(cls, id_number):
        """校验身份证是否正确"""
        if re.match(const.ID_NUMBER_18_REGEX, id_number):
            check_digit = cls(id_number).get_check_digit()
            return str(check_digit) == id_number[-1]
        else:
            return bool(re.match(const.ID_NUMBER_15_REGEX, id_number))

    @classmethod
    def generate_id(cls, sex=0):
        """随机生成身份证号，sex = 0表示女性，sex = 1表示男性"""

        # 随机生成一个区域码(6位数)
        id_number = str(random.choice(list(const.AREA_INFO.keys())))
        # 限定出生日期范围(8位数)
        start, end = datetime.strptime("1960-01-01", "%Y-%m-%d"), datetime.strptime("2000-12-30", "%Y-%m-%d")
        birth_days = datetime.strftime(start + timedelta(random.randint(0, (end - start).days + 1)), "%Y%m%d")
        id_number += str(birth_days)
        # 顺序码(2位数)
        id_number += str(random.randint(10, 99))
        # 性别码(1位数)
        id_number += str(random.randrange(sex, 10, step=2))
        # 校验码(1位数)
        return id_number + str(cls(id_number).get_check_digit())


random_sex = random.randint(0, 1)  # 随机生成男(1)或女(0)
identity = IdNumber.generate_id(random_sex)
age = IdNumber(identity).get_age()
birthday = IdNumber(identity).get_birthday()
sex = IdNumber(identity).get_sex()
area = IdNumber(identity).get_area_name()
area_id = IdNumber(identity).area_id

if __name__ == '__main__':
    print(f"身份证号码：{identity}")  # 随机生成身份证号
    print(f"地址编码：{IdNumber(identity).area_id}")  # 地址编码:410326
    print(f"地址：{IdNumber(identity).get_area_name()}")  # 地址:河南省洛阳市汝阳县
    print(f"生日：{IdNumber(identity).get_birthday()}")  # 生日:1995-7-10
    print(f"年龄：{IdNumber(identity).get_age()}")  # 年龄:23(岁)
    print(f"性别：{IdNumber(identity).get_sex()}")  # 性别:1(男)
    print(f"校验码：{IdNumber(identity).get_check_digit()}")  # 校验码:7
    print(f"检验身份证是否正确：{IdNumber.verify_id(identity)}")  # 检验身份证是否正确:False
