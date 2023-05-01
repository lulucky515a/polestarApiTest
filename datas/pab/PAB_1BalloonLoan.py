# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: PAB_1BalloonLoan.py
# @Author: Luke
# @Time: 4月 25, 2023


from datas.pab import Order, pro_conFig, get_order_info, PABLoan, TradeDateTime


class PABBalloonLoan(PABLoan):
    """
    金融计算器-平安-气球贷款
    """

    def __init__(self, FinanceOrderId, ArchivesCode, RepayLimit, ProductCode, GuarantyType,
                 ApproveYearRate, ApproveLoanAmt, TotalPrice, OrderId, CarType, downPaymentPR, finalPaymentPR,
                 finalPaymentPrice):
        super().__init__(FinanceOrderId, ArchivesCode, RepayLimit, ProductCode, GuarantyType,
                         ApproveYearRate, ApproveLoanAmt, TotalPrice, OrderId, CarType)
        self.downPaymentPR = downPaymentPR
        self.finalPaymentPR = finalPaymentPR
        self.finalPaymentPrice = finalPaymentPrice

    def calculator_balloon_loan_price(self):
        # RepayLimit=60
        mid_payment_loan_amount = round(self.TotalPrice * (1 - self.downPaymentPR / 100 - self.finalPaymentPR / 100))
        final_payment_loan_amount = round(self.TotalPrice * self.finalPaymentPR / 100)
        return mid_payment_loan_amount, final_payment_loan_amount

    def loan_review_20006_body(self):
        loan_review_20006_body = {
            "OrderId": self.FinanceOrderId,
            "ArchivesCode": self.ArchivesCode,
            "ExternalStatus": 20006,
            "TradeDate": TradeDateTime()[0]
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
                    "ApproveLoanAmt": self.calculator_balloon_loan_price()[0],
                    "RepayLimit": self.RepayLimit,
                    "ProductCode": self.ProductCode,
                    "GuarantyType": self.GuarantyType,
                    "ApproveYearRate": self.ApproveYearRate,
                    "IsMainProduct": "Y",
                    "DiscountAmount": "4624.9"
                },
                {
                    # "ApproveLoanAmt": self.calculator_balloon_loan_price()[1],
                    "ApproveLoanAmt": self.finalPaymentPrice,
                    "RepayLimit": self.RepayLimit,
                    "ProductCode": self.ProductCode,
                    "GuarantyType": self.GuarantyType,
                    "ApproveYearRate": self.ApproveYearRate,
                    "IsMainProduct": "N",
                    "DiscountAmount": "3699.9"
                }
            ]
        }
        return loan_review_20009_body

    def loan_review_20013_body(self):
        loan_review_20013_body = [{
            "Date": TradeDateTime(mins=4)[0],
            "ArchivesCode": self.ArchivesCode,
            "ApplCde": self.ArchivesCode,
            "ApproveLoanAmt": self.calculator_balloon_loan_price()[0],
            "RepayLimit": self.RepayLimit,
            "FactoryRate": self.ApproveYearRate,
            "GuarantyType": self.GuarantyType,
            "DiscountAmount": "5000.00",
            "IsMainProduct": "Y"
        },
            {
                "Date": TradeDateTime(mins=4)[0],
                "ArchivesCode": self.ArchivesCode,
                "ApplCde": self.ArchivesCode,
                # "ApproveLoanAmt": self.calculator_balloon_loan_price()[1],
                "ApproveLoanAmt": self.finalPaymentPrice,
                "RepayLimit": self.RepayLimit,
                "FactoryRate": self.ApproveYearRate,
                "GuarantyType": self.GuarantyType,
                "DiscountAmount": "5000.00",
                "IsMainProduct": "N"
            }]
        return loan_review_20013_body


order_info = Order(order_info=get_order_info(), id_number=pro_conFig.getValue('PAB_BL', 'ArchivesCode'))
PAB_1BL_info = PABBalloonLoan(FinanceOrderId=order_info.order()[1], ArchivesCode=order_info.order()[2],
                              RepayLimit=order_info.loan_order_detail()["duration"],
                              ProductCode=order_info.loan_order_detail()["loanOfferId"],
                              GuarantyType=pro_conFig.getValue('PAB_BL', 'GuarantyType'),
                              ApproveYearRate=order_info.loan_order_detail()["customerAPR"] / 100,
                              ApproveLoanAmt=order_info.loan_order_detail()["installmentPrice"],
                              # price=pro_conFig.getValue('PAB_BL', 'price'),
                              downPaymentPR=order_info.loan_order_detail()["downPaymentPR"],
                              finalPaymentPR=order_info.loan_order_detail()["finalPaymentPR"],
                              OrderId=order_info.order()[0],
                              CarType=order_info.loan_order_detail()["vehicleId"],
                              TotalPrice=order_info.loan_order_detail()["totalPrice"],
                              finalPaymentPrice=order_info.loan_order_detail()['finalPaymentPrice'])
if __name__ == '__main__':
    print(f"气球贷的中段贷款金额为：{PAB_1BL_info.calculator_balloon_loan_price()[0]}\n"
          # f"尾款贷款金额为：{PAB_1BL_info.calculator_balloon_loan_price()[1]}")
          f"尾款贷款金额为：{order_info.loan_order_detail()['finalPaymentPrice']}")

    PAB_1BL_list = {"case_id": 2, "title": "平安-金融贷款-气球贷款",
                    "ArchivesCode": PAB_1BL_info.others_info()[0],
                    "OrderId": PAB_1BL_info.others_info()[1],
                    "CarType": PAB_1BL_info.others_info()[2],
                    "FinanceOrderId": PAB_1BL_info.others_info()[3],
                    "TotalPrice": PAB_1BL_info.others_info()[4],
                    "PAB": [PAB_1BL_info.loan_review_20006_body(),
                            PAB_1BL_info.loan_review_20009_body(),
                            PAB_1BL_info.loan_review_20013_body()]}
    print(PAB_1BL_list)
