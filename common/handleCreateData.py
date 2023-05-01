# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: test01_preEmpBaseInfo.py
# @Author: Luke
# @Time: 3月 31, 2023


import time
import random
import string
from faker import Faker


def randomNumber():
    seeds = string.digits
    number = "".join(random.sample(seeds, k=7))
    return number


def timeNumber():
    t = time.time()
    return str(int(round(t * 1000)))


class CreateData:
    def __init__(self):
        self.fk = Faker(locale='zh-CN')

    def name(self):
        return self.fk.name()

    def phone(self):
        return self.fk.phone_number()

    def email(self):
        return self.fk.email()

    def country(self):
        return self.fk.country()

    def province(self):
        """
        省份
        :return:
        """
        return self.fk.province()

    def address(self):
        return self.fk.address()

    def company(self):
        return self.fk.company()

    def city(self):
        return self.fk.city()

    def zip(self):
        code = ''.join([str(random.choice([random.randrange(10)])) for i in range(6)])
        return code

    def ids(self):
        return self.fk.ssn()


UID = timeNumber()
numbers = randomNumber()
createData = CreateData()

if __name__ == '__main__':
    pass
    # print(UID)
    # print(numbers)
    # print(createData.zip())
    # print(createData.province())
    # print(createData.address())
    # print(createData.company())
    # print(createData.ids())
