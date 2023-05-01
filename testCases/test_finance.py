# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: test_login.py
# @Author: Luke
# @Time: 3月 31, 2023


import warnings
import unittest
from testCases import ddt, list_data, DoExcel, caseLog, Request, \
    PAB_0SL_list_0, PAB_0SL_list_1, PAB_0SL_list_2, \
    PAB_1BL_list_0, PAB_1BL_list_1, PAB_1BL_list_2, \
    PAB_2FAL_list_0, PAB_2FAL_list_1, PAB_2FAL_list_2


@ddt
class FinanceTest(unittest.TestCase):
    doExcelPage = DoExcel(sheet_name="financeRecord")
    caseList = [PAB_0SL_list_0, PAB_0SL_list_1, PAB_0SL_list_2,
                PAB_1BL_list_0, PAB_1BL_list_1, PAB_1BL_list_2,
                PAB_2FAL_list_0, PAB_2FAL_list_1, PAB_2FAL_list_2]

    @classmethod
    def setUpClass(cls):
        warnings.simplefilter('ignore', ResourceWarning)
        cls.request = Request()

    def setUp(self):
        caseLog.info('{:=^80s}'.format('Test Finance Start'))

    def tearDown(self):
        caseLog.info('{:=^80s}'.format('Test Finance End'))

    @classmethod
    def tearDownClass(cls):
        cls.request.session.close()

    @list_data(caseList)
    def test_finance(self, case):
        caseLog.info("开始执行第{}条用例: {}".format(case["case_id"], case["title"]))
        print(f'标题：\n{case["title"]}')
        print(f'订单编号：\n{case["ArchivesCode"]}')
        print(f'车辆订单编号：\n{case["OrderId"]}')
        print(f'车辆类型：\n{case["CarType"]}')
        print(f'金融订单编号：\n{case["FinanceOrderId"]}')
        print(f'车辆价格：\n{case["TotalPrice"]}')
        print(f'20006：\n{case["PAB"][0]}')
        print(f'20009：\n{case["PAB"][1]}')
        print(f'20013: \n{case["PAB"][2]}')
        self.doExcelPage.writeDatas(row=case["case_id"] + 1, orderNumber=case["ArchivesCode"], orderID=case["OrderId"],
                                    carType=case["CarType"], financeOrder=case["FinanceOrderId"],
                                    price=case["TotalPrice"], finance20006=str(case["PAB"][0]),
                                    finance20009=str(case["PAB"][1]), finance20013=str(case["PAB"][2]))
