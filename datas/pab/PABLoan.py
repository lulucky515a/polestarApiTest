# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: PABLoan.py
# @Author: Luke
# @Time: 4月 27, 2023


from common.handleData import TradeDateTime


class PABLoan:
    def __init__(self, FinanceOrderId, ArchivesCode, RepayLimit, ProductCode, GuarantyType,
                 ApproveYearRate, ApproveLoanAmt, TotalPrice, OrderId, CarType):
        self.FinanceOrderId = FinanceOrderId
        self.ArchivesCode = ArchivesCode
        self.RepayLimit = RepayLimit
        self.ProductCode = ProductCode
        self.GuarantyType = GuarantyType
        self.ApproveYearRate = ApproveYearRate
        self.ApproveLoanAmt = ApproveLoanAmt
        self.TotalPrice = TotalPrice
        self.OrderId = OrderId
        self.CarType = CarType

    def loan_review_20006_body(self):
        loan_review_20006_body = {
            "OrderId": self.FinanceOrderId,
            "ArchivesCode": self.ArchivesCode,
            "ExternalStatus": 20006,
            "TradeDate": TradeDateTime()[0],
            "LoanList": [
                {
                    "ApproveLoanAmt": self.ApproveLoanAmt,
                    "RepayLimit": self.RepayLimit,
                    "ProductCode": self.ProductCode,
                    "GuarantyType": self.GuarantyType,
                    "ApproveYearRate": self.ApproveYearRate,
                    "IsMainProduct": "Y",
                    "DiscountAmount": "5000.00"
                }
            ]
        }
        return loan_review_20006_body

    def loan_review_20009_body(self):
        loan_review_20009_body = {
            "OrderId": self.FinanceOrderId,
            "ArchivesCode": self.ArchivesCode,
            "ExternalStatus": 20009,
            "TradeDate": TradeDateTime(mins=2)[0],
            "LoanList": [
                {
                    "ApproveLoanAmt": self.ApproveLoanAmt,
                    "RepayLimit": self.RepayLimit,
                    "ProductCode": self.ProductCode,
                    "GuarantyType": self.GuarantyType,
                    "ApproveYearRate": self.ApproveYearRate,
                    "IsMainProduct": "Y",
                    "DiscountAmount": "5000.00"
                }
            ]
        }
        return loan_review_20009_body

    def loan_review_20013_body(self):
        loan_review_20013_body = {
            "Date": TradeDateTime(mins=4)[0],
            "ArchivesCode": self.ArchivesCode,
            "ApplCde": self.ArchivesCode,
            "ApproveLoanAmt": self.ApproveLoanAmt,
            "RepayLimit": self.RepayLimit,
            "FactoryRate": self.ApproveYearRate,
            "GuarantyType": self.GuarantyType,
            "DiscountAmount": "5000.00",
            "IsMainProduct": "Y"
        }
        return loan_review_20013_body

    def others_info(self):
        return self.ArchivesCode, self.OrderId, self.CarType, self.FinanceOrderId, self.TotalPrice
