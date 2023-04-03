# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: handleWebhook.py
# @Author: Luke
# @Time: 3月 31, 2023


import json
import requests
from datetime import datetime
from common import handleContants
from common.handleContants import reportsDir


URL = "http://localhost:63342" + "/" + reportsDir.split(sep="/", maxsplit=4)[-1] + "/" + handleContants.path


def markDown():
    a_title = "<font color=\"info\">自动化测试:</font>\n"
    a_url = f"> 测试结果报告: <font color=\"comment\">[报告地址]({URL})</font>\n"
    b_time = "> 执行时间： < font color =\"comment\">%s</font>\n" % str(datetime.now()).split(".")[0]
    msg = a_title + a_url + b_time
    return json.dumps(msg)


def testWxWebhook():
    data = '{ "msgtype": "markdown", "markdown": { "content": %s } }' % markDown()
    print(data)
    response = requests.post(
        url="https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=6b11dc23-4d98-45e0-89a2-66279025cb7b",
        headers={'Content-Type': 'application/json'}, data=data)
    print(response.text)


if __name__ == '__main__':
    testWxWebhook()