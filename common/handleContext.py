# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: handleContext.py
# @Author: Luke
# @Time: 3月 31, 2023


import re
import random
import datetime
from common.handleConfig import conFig, bpmFig
from common.handleCreateData import createData, numbers, UID, randomNumber
from common.identity.identity import IdNumber
# from common.handleAccount_NEw import get_value


startDay = str(datetime.date.today())


class Context:
    # login
    unionid = conFig.getValue('LoginInfo', 'unionid')
    """
    # ------ 0201-写入薪资 ------
    PreEntryFlowSalary_OFFER_ID = "F" + UID
    PreEntryFlowSalary_OFFER_ID_NEW = "S" + UID
    PreEntryFlowSalary_OFFER_ID_SECOND = "T" + UID
    PreEntryFlowSalary_PROBATION_SALARY = conFig.getValue('preEntryFlowSalary', 'PROBATION_SALARY')
    PreEntryFlowSalary_STANDARD_SALARY = conFig.getValue('preEntryFlowSalary', 'STANDARD_SALARY')
    PreEntryFlowSalary_FREQUENCY_D = conFig.getValue('preEntryFlowSalary', 'FREQUENCY_D')
    PreEntryFlowSalary_FREQUENCY_M = conFig.getValue('preEntryFlowSalary', 'FREQUENCY_M')
    PreEntryFlowSalary_LAST_UPDATE_ID = conFig.getValue('preEntryFlowSalary', 'LAST_UPDATE_ID')
    PreEntryFlowSalary_UPDATE_TIME = startDay

    # ------ 0202-查询薪资 ------
    queryEmpOfferSalary_OFFER_ID = conFig.getValue('rsa', 'OFFER_ID')
    # 解密薪资
    rsa_privateKey = conFig.getValue('rsa', 'privateKey')

    # ------ 0601-入职流程 ------
    # 生成工号
    preCreateEmpNumInfo_NAME = "Test" + numbers
    preCreateEmpNumInfo_NATIONAL_ID_TYPE = conFig.getValue('preCreateEmpNumInfo', 'NATIONAL_ID_TYPE')
    preCreateEmpNumInfo_NATIONAL_ID = IdNumber.generate_id(random.randint(0, 1))
    preCreateEmpNumInfo_COUNTRY = conFig.getValue('preCreateEmpNumInfo', 'COUNTRY')
    # preCreateEmpNumInfo_FLOW_NO = "PCE" + bpmFig.getValue("empInfo1", "flow_no")
    preCreateEmpNumInfo_FLOW_NO = "PCE" + str(IdNumber.generate_id(random.randint(0, 1)))
    # ------ 0603-续签 ------
    RENEW_ADDRESS1 = createData.address()
    RENEW_ZIP_CODE = createData.zip()
    # 首选项
    RENEW_ADDRESS_IS_PRIMARY = conFig.getValue('renewalEmpContractInfo', 'ADDRESS_IS_PRIMARY')
    # [EMP_EMAIL_LIST]
    RENEW_EMAIL_TYPE = conFig.getValue('renewalEmpContractInfo', 'EMAIL_TYPE')
    RENEW_EMAIL_ADDRESS = createData.email()
    RENEW_EMAIL_IS_PRIMARY = conFig.getValue('renewalEmpContractInfo', 'EMAIL_IS_PRIMARY')
    # [EMP_PHONE_LIST]
    RENEW_PHONE_TYPE = conFig.getValue('renewalEmpContractInfo', 'PHONE_TYPE')
    RENEW_PHONE_NUMBER = createData.phone()
    RENEW_PHONE_IS_PRIMARY = conFig.getValue('renewalEmpContractInfo', 'PHONE_IS_PRIMARY')
    """

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
