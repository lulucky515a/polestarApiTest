# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: test_login.py
# @Author: Luke
# @Time: 3月 31, 2023


import warnings
import unittest
from unittestreport import ddt, list_data

from common.handleConfig import conFig
from common.handleContext import Context
from common.handleExcel import DoExcel
from common.handleLogger import caseLog
from common.handleRequest import Request
# from datas.getToken import token


@ddt
class LoginTest(unittest.TestCase):
    doExcelPage = DoExcel(sheet_name="01login")
    casePage = doExcelPage.read_datas()

    @classmethod
    def setUpClass(cls):
        warnings.simplefilter('ignore', ResourceWarning)
        cls.request = Request()

    def setUp(self):
        caseLog.info('{:=^80s}'.format('Test Query Offer Salary Exceed Start'))

    def tearDown(self):
        caseLog.info('{:=^80s}'.format('Test Query Offer Salary Exceed End'))

    @classmethod
    def tearDownClass(cls):
        cls.request.session.close()

    @list_data(casePage)
    def test_login(self, case):
        caseLog.info("开始执行第{}条用例: {}".format(case["case_id"], case["title"] + ' ' + case['url']))
        url = conFig.getValue('URL', 'base_url') + case["url"]

        if case['data'] is not None:
            data_new = Context().replace_new(case["data"])
            caseLog.info(f"动态获取的参数：{data_new}")
        else:
            data_new = case["data"]

        # self.head = {}
        # if case["api"] == "auth":
        #     self.head["Authorization"] = "Bearer"
        # else:
        #     self.head["Authorization"] = "Bearer" + " " + token
        self.head = conFig.getValue('Headers', 'headers')

        resp = self.request.request(case["method"], url, data=data_new, headers=self.head, verify=False)

        try:
            print(f'预期结果：{case["expected"]}')
            self.assertIn(case["expected"], resp.text, f"api info： {case['url']} {case['title']} error")
            self.doExcelPage.writeData(case["case_id"] + 1, resp.text, 'PASS')
            caseLog.info("第{0}用例执行结果：PASS".format(case["case_id"]))
            print(f'实际结果：{resp.text}')
        except AssertionError as e:
            self.doExcelPage.writeData(case["case_id"] + 1, resp.text, 'FAIL')
            caseLog.error("第{0}用例执行结果：FAIL".format(case["case_id"]))
            caseLog.error("断言出错了".format(e))
            raise e