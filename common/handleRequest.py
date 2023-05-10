# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: handleRequest.py
# @Author: Luke
# @Time: 3月 31, 2023


import requests
import json


class Request:

    def __init__(self):
        self.session = requests.sessions.session()

    def request(self, method, url, data=None, headers=None, auth=None, verify=True):
        method = method.upper()

        # if data is not None and type(data) == str:
        #     data = json.loads(data)
        if data is not None and type(data) == str:
            try:
                data = json.loads(data)
            except json.decoder.JSONDecodeError as e:
                print("Failed to parse request data as JSON, exception info:", e)
        if headers is not None and type(headers) == str:
            headers = json.loads(headers)

        print('method: {0} \nurl: {1}'.format(method, url))
        print('data: {0} '.format(data))
        print('headers: {0}'.format(headers))

        if method == "GET":
            return self.session.request(method, url=url, params=data, headers=headers, auth=auth, verify=verify)
        elif method == "POST":
            return self.session.request(method, url=url, json=data, headers=headers, auth=auth, verify=verify)
        elif method == "PUT":
            return self.session.request(method, url=url, json=data, headers=headers, auth=auth, verify=verify)
        else:
            print("Un-support method !!!")


if __name__ == '__main__':
    res = Request()
    result = res.session.request("post", "https://services.stgapi.polestar.cn/api/auth/wechat",
                                 headers={"Content-Type": "application/json"},
                                 # json={"unionid": "oJg1d1nnT9Ve9TjBsoDr3Ua5GGWw"})
                                 json={"unionid": "ghgjj"})
    # print(result.json()["mobile"])
    print(result.text)
    # {'message': 'unionid is required'}



