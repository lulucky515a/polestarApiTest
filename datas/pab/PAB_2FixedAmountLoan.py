# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: PAB_2FixedAmountLoan.py
# @Author: Luke
# @Time: 4月 25, 2023


from datas.pab import Order, pro_conFig, get_order_info, PABLoan


class PABFixedAmountLoan(PABLoan):
    """
    金融计算器-平安-定额贷款
    """
    pass


order_info = Order(order_info=get_order_info(), id_number=pro_conFig.getValue('PAB_FAL', 'ArchivesCode'))
PAB_2FAL_info = PABFixedAmountLoan(FinanceOrderId=order_info.order()[1], ArchivesCode=order_info.order()[2],
                                   RepayLimit=order_info.loan_order_detail()["duration"],
                                   ProductCode=order_info.loan_order_detail()["loanOfferId"],
                                   GuarantyType=pro_conFig.getValue('PAB_FAL', 'GuarantyType'),
                                   ApproveYearRate=order_info.loan_order_detail()["customerAPR"] / 100,
                                   ApproveLoanAmt=order_info.loan_order_detail()["installmentPrice"],
                                   OrderId=order_info.order()[0],
                                   CarType=order_info.loan_order_detail()["vehicleId"],
                                   TotalPrice=order_info.loan_order_detail()["totalPrice"])
if __name__ == '__main__':
    PAB_2FAL_list = {"case_id": 3, "title": "平安-金融贷款-定额贷款",
                     "ArchivesCode": PAB_2FAL_info.others_info()[0],
                     "OrderId": PAB_2FAL_info.others_info()[1],
                     "CarType": PAB_2FAL_info.others_info()[2],
                     "FinanceOrderId": PAB_2FAL_info.others_info()[3],
                     "TotalPrice": PAB_2FAL_info.others_info()[4],
                     "PAB": [PAB_2FAL_info.loan_review_20006_body(),
                             PAB_2FAL_info.loan_review_20009_body(),
                             PAB_2FAL_info.loan_review_20013_body()]}
    print(PAB_2FAL_list)
