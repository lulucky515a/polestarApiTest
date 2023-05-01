# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: __init__.py.py
# @Author: Luke
# @Time: 3月 31, 2023


# test_finance.py
from unittestreport import ddt, list_data
from common.handleExcel import DoExcel
from common.handleLogger import caseLog
from common.handleRequest import Request
from datas.pab import PAB_0StandardLoan, PAB_1BalloonLoan, PAB_2FixedAmountLoan

# test_login.py
# from unittestreport import ddt, list_data
from common.handleConfig import conFig
from common.handleContext import Context
# from common.handleExcel import DoExcel
# from common.handleLogger import caseLog
# from common.handleRequest import Request


# test_finance
PAB_0SL_list_0 = {"case_id": 1, "title": "平安-金融贷款-标准贷款",
                  "ArchivesCode": PAB_0StandardLoan.PAB_0SL_info.others_info()[0],
                  "OrderId": PAB_0StandardLoan.PAB_0SL_info.others_info()[1],
                  "CarType": PAB_0StandardLoan.PAB_0SL_info.others_info()[2],
                  "FinanceOrderId": PAB_0StandardLoan.PAB_0SL_info.others_info()[3],
                  "TotalPrice": PAB_0StandardLoan.PAB_0SL_info.others_info()[4],
                  "PAB": [PAB_0StandardLoan.PAB_0SL_info.loan_review_20006_body(),
                          PAB_0StandardLoan.PAB_0SL_info.loan_review_20009_body(),
                          PAB_0StandardLoan.PAB_0SL_info.loan_review_20013_body()]}
PAB_0SL_list_1 = {"case_id": 2, "title": "平安-金融贷款-标准贷款-气球贷款",
                  "ArchivesCode": PAB_0StandardLoan.PAB_0SL_info.others_info()[0],
                  "OrderId": PAB_0StandardLoan.PAB_0SL_info.others_info()[1],
                  "CarType": PAB_0StandardLoan.PAB_0SL_info.others_info()[2],
                  "FinanceOrderId": PAB_0StandardLoan.PAB_0SL_info.others_info()[3],
                  "TotalPrice": PAB_0StandardLoan.PAB_0SL_info.others_info()[4],
                  "PAB": [PAB_0StandardLoan.PAB_0SL_info.loan_review_20006_body(),
                          PAB_1BalloonLoan.PAB_1BL_info.loan_review_20009_body(),
                          PAB_1BalloonLoan.PAB_1BL_info.loan_review_20013_body()]}
PAB_0SL_list_2 = {"case_id": 3, "title": "平安-金融贷款-标准贷款-定额贷款",
                  "ArchivesCode": PAB_0StandardLoan.PAB_0SL_info.others_info()[0],
                  "OrderId": PAB_0StandardLoan.PAB_0SL_info.others_info()[1],
                  "CarType": PAB_0StandardLoan.PAB_0SL_info.others_info()[2],
                  "FinanceOrderId": PAB_0StandardLoan.PAB_0SL_info.others_info()[3],
                  "TotalPrice": PAB_0StandardLoan.PAB_0SL_info.others_info()[4],
                  "PAB": [PAB_0StandardLoan.PAB_0SL_info.loan_review_20006_body(),
                          PAB_2FixedAmountLoan.PAB_2FAL_info.loan_review_20009_body(),
                          PAB_2FixedAmountLoan.PAB_2FAL_info.loan_review_20013_body()]}
PAB_1BL_list_0 = {"case_id": 4, "title": "平安-金融贷款-气球贷款",
                  "ArchivesCode": PAB_1BalloonLoan.PAB_1BL_info.others_info()[0],
                  "OrderId": PAB_1BalloonLoan.PAB_1BL_info.others_info()[1],
                  "CarType": PAB_1BalloonLoan.PAB_1BL_info.others_info()[2],
                  "FinanceOrderId": PAB_1BalloonLoan.PAB_1BL_info.others_info()[3],
                  "TotalPrice": PAB_1BalloonLoan.PAB_1BL_info.others_info()[4],
                  "PAB": [PAB_1BalloonLoan.PAB_1BL_info.loan_review_20006_body(),
                          PAB_1BalloonLoan.PAB_1BL_info.loan_review_20009_body(),
                          PAB_1BalloonLoan.PAB_1BL_info.loan_review_20013_body()]}
PAB_1BL_list_1 = {"case_id": 5, "title": "平安-金融贷款-气球贷款-标准贷款",
                  "ArchivesCode": PAB_1BalloonLoan.PAB_1BL_info.others_info()[0],
                  "OrderId": PAB_1BalloonLoan.PAB_1BL_info.others_info()[1],
                  "CarType": PAB_1BalloonLoan.PAB_1BL_info.others_info()[2],
                  "FinanceOrderId": PAB_1BalloonLoan.PAB_1BL_info.others_info()[3],
                  "TotalPrice": PAB_1BalloonLoan.PAB_1BL_info.others_info()[4],
                  "PAB": [PAB_1BalloonLoan.PAB_1BL_info.loan_review_20006_body(),
                          PAB_0StandardLoan.PAB_0SL_info.loan_review_20009_body(),
                          PAB_0StandardLoan.PAB_0SL_info.loan_review_20013_body()]}
PAB_1BL_list_2 = {"case_id": 6, "title": "平安-金融贷款-气球贷款-定额贷款",
                  "ArchivesCode": PAB_1BalloonLoan.PAB_1BL_info.others_info()[0],
                  "OrderId": PAB_1BalloonLoan.PAB_1BL_info.others_info()[1],
                  "CarType": PAB_1BalloonLoan.PAB_1BL_info.others_info()[2],
                  "FinanceOrderId": PAB_1BalloonLoan.PAB_1BL_info.others_info()[3],
                  "TotalPrice": PAB_1BalloonLoan.PAB_1BL_info.others_info()[4],
                  "PAB": [PAB_1BalloonLoan.PAB_1BL_info.loan_review_20006_body(),
                          PAB_2FixedAmountLoan.PAB_2FAL_info.loan_review_20009_body(),
                          PAB_2FixedAmountLoan.PAB_2FAL_info.loan_review_20013_body()]}
PAB_2FAL_list_0 = {"case_id": 7, "title": "平安-金融贷款-定额贷款",
                   "ArchivesCode": PAB_2FixedAmountLoan.PAB_2FAL_info.others_info()[0],
                   "OrderId": PAB_2FixedAmountLoan.PAB_2FAL_info.others_info()[1],
                   "CarType": PAB_2FixedAmountLoan.PAB_2FAL_info.others_info()[2],
                   "FinanceOrderId": PAB_2FixedAmountLoan.PAB_2FAL_info.others_info()[3],
                   "TotalPrice": PAB_2FixedAmountLoan.PAB_2FAL_info.others_info()[4],
                   "PAB": [PAB_2FixedAmountLoan.PAB_2FAL_info.loan_review_20006_body(),
                           PAB_2FixedAmountLoan.PAB_2FAL_info.loan_review_20009_body(),
                           PAB_2FixedAmountLoan.PAB_2FAL_info.loan_review_20013_body()]}
PAB_2FAL_list_1 = {"case_id": 8, "title": "平安-金融贷款-定额贷款-标准贷款",
                   "ArchivesCode": PAB_2FixedAmountLoan.PAB_2FAL_info.others_info()[0],
                   "OrderId": PAB_2FixedAmountLoan.PAB_2FAL_info.others_info()[1],
                   "CarType": PAB_2FixedAmountLoan.PAB_2FAL_info.others_info()[2],
                   "FinanceOrderId": PAB_2FixedAmountLoan.PAB_2FAL_info.others_info()[3],
                   "TotalPrice": PAB_2FixedAmountLoan.PAB_2FAL_info.others_info()[4],
                   "PAB": [PAB_2FixedAmountLoan.PAB_2FAL_info.loan_review_20006_body(),
                           PAB_0StandardLoan.PAB_0SL_info.loan_review_20009_body(),
                           PAB_0StandardLoan.PAB_0SL_info.loan_review_20013_body()]}
PAB_2FAL_list_2 = {"case_id": 9, "title": "平安-金融贷款-定额贷款-气球贷款",
                   "ArchivesCode": PAB_2FixedAmountLoan.PAB_2FAL_info.others_info()[0],
                   "OrderId": PAB_2FixedAmountLoan.PAB_2FAL_info.others_info()[1],
                   "CarType": PAB_2FixedAmountLoan.PAB_2FAL_info.others_info()[2],
                   "FinanceOrderId": PAB_2FixedAmountLoan.PAB_2FAL_info.others_info()[3],
                   "TotalPrice": PAB_2FixedAmountLoan.PAB_2FAL_info.others_info()[4],
                   "PAB": [PAB_2FixedAmountLoan.PAB_2FAL_info.loan_review_20006_body(),
                           PAB_1BalloonLoan.PAB_1BL_info.loan_review_20009_body(),
                           PAB_1BalloonLoan.PAB_1BL_info.loan_review_20013_body()]}


if __name__ == '__main__':
    pass
