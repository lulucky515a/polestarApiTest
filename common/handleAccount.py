# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: handleAccount.py
# @Author: Luke
# @Time: 3月 31, 2023


import datetime
import json
import random

from common import handleContants
from common.handleRequest import Request
from common.handleLogger import caseLog
from common.handleConfig import conFig, writeConfig
from common.identity.identity import random_sex, IdNumber
from common.handleCreateData import createData, timeNumber, randomNumber
from datas.getToken import token


startDay = str(datetime.date.today())


class CreatEmployee(object):
    request = Request()
    objectList = []
    count = 0
    accountData = {}

    @staticmethod
    def __new__(cls, *args, **kwargs):
        while cls.count < 1:
            cls.__object = super().__new__(cls)

            identity = IdNumber.generate_id(random.randint(0, 1))
            headers = {"Authorization": f"Bearer {token}"}
            url = conFig.getValue('URL', 'base_url') + conFig.getValue('empAccount', 'numberUrl')
            body = {
                    "NAME": f"测试-{createData.name()}",
                    "NATIONAL_ID_TYPE": "NID",
                    "NATIONAL_ID": identity,
                    "COUNTRY": "CHN",
                    "FLOW_NO": timeNumber()
                    }
            try:
                res = cls.request.request(url=url, method='post', headers=headers, data=body)
            except Exception as e:
                raise e
            caseLog.info(f"生成的预入职的员工信息：{res.json()}")
            emp_number = res.json()['DATA']['EMPLOYEE_NUMBER']
            is_resign = res.json()['DATA']['IS_RESIGN']
            emp_number_url = conFig.getValue('URL', 'base_url') + conFig.getValue('empAccount', 'returnNumberUrl')

            with open(handleContants.empBody, "r", encoding="utf-8") as f2:
                emp_data = json.loads(f2.read())
            emp_data["EMPLOYEE_NUMBER"] = emp_number
            # emp_data["NAME"] = f"中电压测{cls.count+100}"
            emp_data["BIRTHDAY"] = IdNumber(identity).get_birthday()
            emp_data["FIRST_NAME"] = f"Api-{randomNumber()}"
            emp_data["GENDER"] = "M" if IdNumber(identity).get_sex() == "male" else "F"
            emp_data["GENDER"] = emp_data["GENDER"][0]
            emp_data["NATIONAL_ID"] = identity
            # emp_data["FLOW_NO"] = f"PEBI{timeNumber()}"
            emp_data["FLOW_NO"] = timeNumber()
            # emp_data["GXSJ"] = startDay

            # EMP_WORK_BASE_LOCAL_LIST
            emp_data["EMP_WORK_BASE_LOCAL_LIST"][0]["ADDRESS1"] = IdNumber(identity).get_area_name()
            emp_data["EMP_WORK_BASE_LOCAL_LIST"][0]["ZIP_CODE"] = IdNumber(identity).area_id
            # EMP_EMAIL_LIST
            emp_data["EMP_EMAIL_LIST"][0]["EMAIL_ADDRESS"] = createData.email()
            # EMP_BANK_ACCT_LIST
            emp_data["EMP_BANK_ACCT_LIST"][0]["BANK_ACCOUNT"] = "62258821" + str(randomNumber())
            emp_data["EMP_BANK_ACCT_LIST"][0]["BANK_ACCOUNT_HOLDER"] = createData.name()
            # EMP_PHONE_LIST
            emp_data["EMP_PHONE_LIST"][0]["PHONE_NUMBER"] = createData.phone()

            try:
                resp = cls.request.request(url=emp_number_url, method='post', headers=headers, data=emp_data)
                if "成功" in resp.json()['ERR_MSG']:
                    employee = {
                        'employee_name': emp_data["FIRST_NAME"],
                        # 'name': emp_data["NAME"],
                        'national_id': emp_data["NATIONAL_ID"],
                        'birthday': emp_data["BIRTHDAY"],
                        'age': IdNumber(identity).get_age(),
                        'sex': emp_data["GENDER"],
                        'area': emp_data["EMP_WORK_BASE_LOCAL_LIST"][0]["ADDRESS1"],
                        'area_id': emp_data["EMP_WORK_BASE_LOCAL_LIST"][0]["ZIP_CODE"],
                        'email': emp_data["EMP_EMAIL_LIST"][0]["EMAIL_ADDRESS"],
                        'phone': emp_data["EMP_PHONE_LIST"][0]["PHONE_NUMBER"],
                        'flow_no': emp_data["FLOW_NO"],
                        'employee_number': emp_data["EMPLOYEE_NUMBER"],
                        'is_resign': is_resign
                        }
                    cls.objectList.append(employee)
                else:
                    return "员工没有创建成功！"
            except Exception as e:
                raise e
            cls.count += 1
        return cls.objectList

    @staticmethod
    def writeCreateAccount():
        for i in range(len(CreatEmployee.objectList)):
            CreatEmployee.accountData.update({f"empInfo{i+1}": CreatEmployee.objectList[i]})

        writeConfig.writeConfig(datas=CreatEmployee.accountData)
        caseLog.info(f"Create Data：{CreatEmployee.accountData}")
        return CreatEmployee.accountData

"""
import ctypes

value = CreatEmployee.writeCreateAccount()  # 定义一个字符串变量

address = id(value)  # 获取value的地址，赋给address
get_value = ctypes.cast(address, ctypes.py_object).value  # 读取地址中的变量
# print(get_value)
# print(type(get_value))
"""

if __name__ == '__main__':
    print(CreatEmployee())
    CreatEmployee.writeCreateAccount()
    # print(get_value,type(get_value))

    # import ctypes
    #
    # value = CreatEmployee.writeCreateAccount  # 定义一个字符串变量
    #
    # address = id(value)  # 获取value的地址，赋给address
    # get_value = ctypes.cast(address, ctypes.py_object).value  # 读取地址中的变量
    # print(get_value)
    # # print(type(get_value))




