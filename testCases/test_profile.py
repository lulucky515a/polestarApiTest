# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: test_profile.py
# @Author: Luke
# @Time: 5月 06, 2023


import json
import warnings
import unittest
from testCases import ddt, list_data, DoExcel, caseLog, Request, conFig, Context, authorization


@ddt
class ProfileTest(unittest.TestCase):
    doExcelPage = DoExcel(sheet_name="profile")
    casePage = doExcelPage.read_datas()

    @classmethod
    def setUpClass(cls):
        warnings.simplefilter('ignore', ResourceWarning)
        cls.request = Request()
        # cls.token = cls.request.request("post",
        #                                 conFig.getValue('URL', 'base_url') + conFig.getValue('URL', 'union_url'),
        #                                 {"unionid": conFig.getValue('LoginInfo', 'unionid')},
        #                                 conFig.getValue('Headers', 'headers'))
        # print(f'Authorization：{cls.token.json()["token"]}')

    def setUp(self):
        caseLog.info('{:=^80s}'.format('Test Profile Start'))

    def tearDown(self):
        caseLog.info('{:=^80s}'.format('Test Profile End'))

    @classmethod
    def tearDownClass(cls):
        cls.request.session.close()

    @list_data(casePage)
    def test_profile(self, case):
        caseLog.info("开始执行第{}条用例: {}".format(case["case_id"], case["title"] + ' ' + case['url']))
        url = conFig.getValue('URL', 'pscnid_url') + case["url"]

        if case['data'] is not None:
            data_new = Context().replace_new(case["data"])
            caseLog.info(f"动态获取的参数：{data_new}")
        else:
            data_new = case["data"]

        self.head = eval(conFig.getValue('Headers', 'headers'))
        if case["api"] == "auth":
            self.head = eval(conFig.getValue('Headers', 'headers'))
            if "错误的" in case["title"]:
                self.head.update({"Authorization": f"Bearer error_token"})
        else:
            # self.head.update({"Authorization": f"Bearer {self.token.json()['token']}"})
            self.head.update(authorization)

        resp = self.request.request(case["method"], url, data=data_new, headers=self.head)

        try:
            print(f'预期结果：{case["expected"]}')
            # self.assertIn(case["expected"], resp.text, f"api info： {case['url']} {case['title']} error")
            self.assertTrue(self.doExcelPage.check_json_keys(resp.text, case["expected"]))
            self.doExcelPage.writeData(case["case_id"] + 1, resp.text, 'PASS')
            caseLog.info("第{0}用例执行结果：PASS".format(case["case_id"]))
            print(f'实际结果：{resp.text}')
        except AssertionError as e:
            self.doExcelPage.writeData(case["case_id"] + 1, resp.text, 'FAIL')
            caseLog.error("第{0}用例执行结果：FAIL".format(case["case_id"]))
            caseLog.error("断言出错了".format(e))
            raise e

