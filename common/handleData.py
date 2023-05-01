# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: handleData.py
# @Author: Luke
# @Time: 4月 25, 2023


import datetime
import jsonpath
import pytz
from common.handleCreateData import numbers
from common import Request, conFig, caseLog


def TradeDateTime(mins=0):
    # 设置本地时间和时区
    local_time = datetime.datetime.now()
    local_timezone = pytz.timezone('Asia/Shanghai')  # 设置中国时区

    # 将本地时间转换为UTC时间
    utc_time = local_time.astimezone(pytz.utc)

    # 加上1分钟
    utc_time = utc_time + datetime.timedelta(minutes=mins)

    # 生成包含微秒的UTC时间字符串
    microsecond = str(utc_time.microsecond).zfill(7)
    utc_time_str = utc_time.strftime('%Y-%m-%dT%H:%M:%S.') + microsecond
    vin_time = utc_time.strftime('%Y%m%dT%H%M%S')

    # 将UTC时间转换为本地时间带时区字符串
    local_time_str = utc_time.astimezone(local_timezone).strftime('%z')

    # 拼接生成最终的时间字符串
    time_format = utc_time_str + local_time_str[:-2] + ':' + local_time_str[-2:]
    return time_format, vin_time


res = Request()
header = eval(conFig.getValue('Headers', 'headers'))
# checkout_order = 21095266
checkout_order = conFig.getValue('PAB_FAL', 'ArchivesCode')


def get_unionid():
    body = {"unionid": conFig.getValue('LoginInfo', 'unionid')}
    try:
        resp = res.session.request(method='POST',
                               url=(conFig.getValue('URL', 'base_url') + conFig.getValue('URL', 'union_url')),
                               json=body, headers=header)
        caseLog.info(f"response: {resp}")
    except Exception as e:
        caseLog.error(f"{e}")
    else:
        return resp.json()["token"]


token = 'Bearer ' + get_unionid()
authorization = {"Authorization": token}
header.update(authorization)


def update_order_status():
    body = {
        "source": "vista",
        "trigger": "order_info_updated",
        "event_type": "order_updated",
        "event_time": TradeDateTime()[0],
        "data": {
            "order_no": checkout_order,
            "orderlines": [
                {
                    "orderline_type": "ConsumerCar",
                    "car_factory_order": {
                        "actual_vista_status_point": "112"
                    }
                }
            ]
        }
    }
    resp = res.session.request(method='POST',
                               url=(conFig.getValue('URL', 'base_url') + conFig.getValue('URL', 'order_status_url')),
                               json=body, headers=header)
    return resp.text


def get_order_info():
    resp = res.session.request(method='GET',
                               url=(conFig.getValue('URL', 'base_url') + conFig.getValue('URL', 'order_url')),
                               headers=header)
    return resp.json()


def get_loan_offer_info():
    resp = res.session.request(method='GET',
                               url=(conFig.getValue('URL', 'base_url') + conFig.getValue('URL', 'loan_offer_url')),
                               headers=header)
    return resp.json()


def get_loan_order_detail(order_id):
    resp = res.session.request(method='GET',
                               url=(conFig.getValue('URL', 'finance_base_url') + conFig.getValue('URL', 'pab_loan_order_url') +
                                    f'/{order_id}'), headers=header)
    return resp.json()


def get_car_order():
    # with open('/Users/luzhixiang/PycharmProjects/polestarApiTest/datas/order.json', 'r') as f:
    #     data = json.load(f)
    data = get_order_info()
    run_list = jsonpath.jsonpath(data, f'$[?(@.pomsid == "{checkout_order}")].id')

    return run_list[0]


def create_vin():
    body = {
        "vin": str(numbers) + TradeDateTime()[1],
        "engineNo": str(numbers) + TradeDateTime()[1] + "test"
    }
    vin_url = conFig.getValue('URL', 'vin_url')
    vin_list = vin_url.split("{}")
    vin_url_finally = vin_list[0] + str(get_car_order()) + vin_list[1]
    resp = res.session.request(method='POST',
                               url=(conFig.getValue('URL', 'base_url') + vin_url_finally),
                               json=body, headers=header)
    return resp.text


if __name__ == '__main__':
    print(TradeDateTime())
    # print(f"获取unionid：{get_unionid()}")
    # print(f"更新订单状态：{update_order_status()}")
    # get_order_info()
    # print(f"获取车辆订单： {get_car_order()}")
    # print(f"生成vin：{create_vin()}")
    print(get_loan_order_detail("b236e8a5-8881-4716-8b64-672750b6a3be"))



