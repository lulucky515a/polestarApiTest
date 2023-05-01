# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: handleCarInfo.py
# @Author: Luke
# @Time: 3月 31, 2023


import jsonpath
from common import pro_conFig, get_order_info, get_loan_offer_info, get_loan_order_detail


class Order:
    """
    获取车辆订单相关信息
    """

    def __init__(self, order_info, id_number):
        self.order_info = order_info
        self.id_number = id_number

    def order(self):
        order_id = jsonpath.jsonpath(self.order_info, f'$[?(@.pomsid == "{self.id_number}")].id')[0]
        # print(f"获取的车辆订单编号为：{order_id}")
        loan_id = jsonpath.jsonpath(self.order_info, f'$[?(@.pomsid == "{self.id_number}")].loanid')[0]
        # print(f"获取的金融订单编号为：{loan_id}")
        return order_id, loan_id, self.id_number

    def car_info(self):
        # 获取车辆信息
        car_info = jsonpath.jsonpath(self.order_info,
                                     f"$[?(@.id=='{self.order()[0]}' && @.loanid=='{self.order()[1]}')]")
        model = car_info[0]["configdetail"]["Summarizes"]
        model_name = "engine"
        model_type_detail = [key["Code"] for key in model if key["Id"] == model_name]
        car_name = (f'{"".join(car_info[0]["configdetail"]["ModelName"].split("-"))}-'
                    f'{car_info[0]["configdetail"]["ModelYear"]}-{model_type_detail[0]}')
        return car_name

    def loan_offer_info(self, provider='PAB'):
        # 获取loan offer info
        loan_info = get_loan_offer_info()
        # provider = 'PAB'
        loan_offer_info = jsonpath.jsonpath(
            loan_info,
            f"$[?(@.provider=='{provider}' && @.vehicleId=='{self.car_info()[:1].upper() + self.car_info()[1:]}')]")
        # print(loan_offer_info)
        return loan_offer_info

    def loan_order_detail(self):
        try:
            loan_detail = get_loan_order_detail(self.order()[1])["data"]
        except Exception as e:
            print(f"订单号码不存在：{e}")
        else:
            loanOfferId = loan_detail["loanOfferId"]
            vehicleId = loan_detail["vehicleId"]  # 车辆型号
            totalPrice = loan_detail["totalPrice"]
            duration = loan_detail["duration"]
            downPaymentPR = loan_detail["downPaymentPR"]  # 首付金额比例
            downPaymentPrice = loan_detail["downPaymentPrice"]  # 首付金额
            installmentPrice = loan_detail["installmentPrice"]  # 贷款金额
            loanName = loan_detail["loanName"]  # 金融产品名称
            applyLoanType = loan_detail["applyLoanType"]  # 金融分类
            customerAPR = loan_detail["customerAPR"]  # 年化利率
            finalPaymentPR = loan_detail["finalPaymentPR"]  # 尾款金额比例-气球贷
            finalPaymentPrice = loan_detail["finalPaymentPrice"]  # 尾款金额
            loan_info = {"loanOfferId": loanOfferId, "vehicleId": vehicleId, "totalPrice": totalPrice,
                         "duration": duration,
                         "downPaymentPR": downPaymentPR, "downPaymentPrice": downPaymentPrice,
                         "installmentPrice": installmentPrice, "loanName": loanName, "applyLoanType": applyLoanType,
                         "customerAPR": customerAPR, "finalPaymentPR": finalPaymentPR,
                         "finalPaymentPrice": finalPaymentPrice}
            return loan_info


if __name__ == '__main__':
    order_info = Order(order_info=get_order_info(), id_number=pro_conFig.getValue('PAB_SL', 'ArchivesCode'))
    # order_info = Order(order_info=get_order_info(), id_number=pro_conFig.getValue('PAB_BL', 'ArchivesCode'))
    # order_info = Order(order_info=get_order_info(), id_number=pro_conFig.getValue('PAB_FAL', 'ArchivesCode'))
    # print(order_info.car_info())
    print(order_info.loan_order_detail())
