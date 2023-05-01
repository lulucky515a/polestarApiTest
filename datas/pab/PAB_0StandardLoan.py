# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: PAB_0StandardLoan.py
# @Author: Luke
# @Time: 4月 25, 2023


from datas.pab import Order, pro_conFig, get_order_info, PABLoan


class PABStandardLoan(PABLoan):
    """
    平安-金融贷款-标准贷款
    """
    pass


order_info = Order(order_info=get_order_info(), id_number=pro_conFig.getValue('PAB_SL', 'ArchivesCode'))
PAB_0SL_info = PABStandardLoan(FinanceOrderId=order_info.order()[1], ArchivesCode=order_info.order()[2],
                               RepayLimit=order_info.loan_order_detail()["duration"],
                               ProductCode=order_info.loan_order_detail()["loanOfferId"],
                               GuarantyType=pro_conFig.getValue('PAB_SL', 'GuarantyType'),
                               ApproveYearRate=order_info.loan_order_detail()["customerAPR"] / 100,
                               ApproveLoanAmt=order_info.loan_order_detail()["installmentPrice"],
                               OrderId=order_info.order()[0],
                               CarType=order_info.loan_order_detail()["vehicleId"],
                               TotalPrice=order_info.loan_order_detail()["totalPrice"])
if __name__ == '__main__':
    PAB_0SL_list = {"case_id": 1, "title": "平安-金融贷款-标准贷款",
                    "ArchivesCode": PAB_0SL_info.others_info()[0],
                    "OrderId": PAB_0SL_info.others_info()[1],
                    "CarType": PAB_0SL_info.others_info()[2],
                    "FinanceOrderId": PAB_0SL_info.others_info()[3],
                    "TotalPrice": PAB_0SL_info.others_info()[4],
                    "PAB": [PAB_0SL_info.loan_review_20006_body(),
                            PAB_0SL_info.loan_review_20009_body(),
                            PAB_0SL_info.loan_review_20013_body()]}
    print(PAB_0SL_list)
