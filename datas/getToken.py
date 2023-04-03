# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: getToken.py
# @Author: Luke
# @Time: 4月 09, 2022


import json

from common.handleRequest import Request
from common.handleLogger import caseLog
from common.handleConfig import conFig


def getToken(url, body=None, header=None, method="post"):
    try:
        res = Request()
        resp = res.session.request(url=url, headers=header, method=method, data=body)
        caseLog.info(f"response: {resp}")
    except Exception as e:
        caseLog.error(f"{e}")
    else:
        return resp


# bpm
bmpBody = {"client_id": conFig.getValue('Headers', 'client_id'),
           "client_secret": conFig.getValue('Headers', 'client_secret'),
           "grant_type": conFig.getValue('Headers', 'grant_type'),
           "scope": conFig.getValue('Headers', 'scope')}
token = getToken(url=(conFig.getValue('URL', 'base_url') + conFig.getValue('URL', 'token_url')),
                 body=bmpBody).json()["access_token"]

# p+
"""
pBody = {"username": conFig.getValue('pInfo', 'username'),
         "password": conFig.getValue('pInfo', 'password'),
         "validCode": eval(conFig.getValue('pInfo', 'validCode')),
         "loginType": conFig.getValue('pInfo', 'loginType')}
pToken = getToken(url=(conFig.getValue('pInfo', 'baseUrl') + conFig.getValue('pInfo', 'loginUrl')),
                  header=eval(conFig.getValue('Headers', 'headers')),
                  body=json.dumps(pBody)).cookies["access_token"]
"""


if __name__ == '__main__':
    print(token)