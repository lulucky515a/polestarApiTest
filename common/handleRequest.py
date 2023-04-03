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

        if data is not None and type(data) == str:
            data = json.loads(data)
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
    # body = {"client_id": "061a280aa5dccb79e2d1735d85f4d574",
    #         "client_secret": "8a16e53a7f434169b876b6664c850720",
    #         "grant_type": "client_credentials",
    #         "scope": "invoke_demo"}
    # result = res.session.request("post", "http://10.99.16.137:10443/integration/api/v1/token", data=body)
    # print(result.status_code)
    # print(result.json())
    # token = result.json()["access_token"]
    result = res.session.request("post", "https://services.stgapi.polestar.cn/api/auth/wechat",
                                 headers={"Content-Type": "application/json"},
                                 # json={"unionid": "oJg1d1nnT9Ve9TjBsoDr3Ua5GGWw"})
                                 json={"unionid": "ghgjj"})
    # print(result.json()["mobile"])
    print(result.text)
    # {'message': 'unionid is required'}
"""
curl 'https://services.stgapi.polestar.cn/api/orders/v2/poms/21095663' \
  -H 'authority: services.stgapi.polestar.cn' \
  -H 'pragma: no-cache' \
  -H 'cache-control: no-cache' \
  -H 'sec-ch-ua: "Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"' \
  -H 'accept: application/json, text/plain, */*' \
  -H 'authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6InpoaXhpYW5nLmx1QHN1cHBsaWVyLnBvbGVzdGFyLmNvbSIsInJvbGVzIjpbImFkbWluIiwiRlNBZG1pbiIsIkRpZ2l0YWxBZG1pbiJdLCJlbWFpbCI6InpoaXhpYW5nLmx1QHN1cHBsaWVyLnBvbGVzdGFyLmNvbSIsInBlcm1pc3Npb25zIjpbeyJtb2R1bGVDb2RlIjoiT3JkZXIiLCJwZXJtaXNzaW9uQ29kZSI6IkFkbWluIiwicGVybWlzc2lvbldlaWdodCI6MzAwMH0seyJtb2R1bGVDb2RlIjoiT3JkZXIgRGV0YWlsIiwicGVybWlzc2lvbkNvZGUiOiJBZG1pbiIsInBlcm1pc3Npb25XZWlnaHQiOjMwMDB9LHsibW9kdWxlQ29kZSI6Ik9yZGVyIEhhbmRvdmVyIiwicGVybWlzc2lvbkNvZGUiOiJBZG1pbiIsInBlcm1pc3Npb25XZWlnaHQiOjMwMDB9LHsibW9kdWxlQ29kZSI6Ik9yZGVyIExvYW4iLCJwZXJtaXNzaW9uQ29kZSI6IkFkbWluIiwicGVybWlzc2lvbldlaWdodCI6MzAwMH0seyJtb2R1bGVDb2RlIjoiT3JkZXIgTGVhc2luZyIsInBlcm1pc3Npb25Db2RlIjoiQWRtaW4iLCJwZXJtaXNzaW9uV2VpZ2h0IjozMDAwfSx7Im1vZHVsZUNvZGUiOiJPcmRlciBQYXltZW50IiwicGVybWlzc2lvbkNvZGUiOiJBZG1pbiIsInBlcm1pc3Npb25XZWlnaHQiOjMwMDB9LHsibW9kdWxlQ29kZSI6Ik9yZGVyIFByb21vIiwicGVybWlzc2lvbkNvZGUiOiJBZG1pbiIsInBlcm1pc3Npb25XZWlnaHQiOjMwMDB9LHsibW9kdWxlQ29kZSI6Ik9yZGVyIFZlaGljbGUiLCJwZXJtaXNzaW9uQ29kZSI6IkFkbWluIiwicGVybWlzc2lvbldlaWdodCI6MzAwMH0seyJtb2R1bGVDb2RlIjoiT3JkZXIgQ29uZmlndXJhdG9yIiwicGVybWlzc2lvbkNvZGUiOiJBZG1pbiIsInBlcm1pc3Npb25XZWlnaHQiOjMwMDB9LHsibW9kdWxlQ29kZSI6Ik9yZGVyIEVzaWduIiwicGVybWlzc2lvbkNvZGUiOiJBZG1pbiIsInBlcm1pc3Npb25XZWlnaHQiOjMwMDB9LHsibW9kdWxlQ29kZSI6Ik9yZGVyIEF1ZGl0IExvZyIsInBlcm1pc3Npb25Db2RlIjoiQWRtaW4iLCJwZXJtaXNzaW9uV2VpZ2h0IjozMDAwfSx7Im1vZHVsZUNvZGUiOiJPcmRlciBTdG9ja0NhciIsInBlcm1pc3Npb25Db2RlIjoiQWRtaW4iLCJwZXJtaXNzaW9uV2VpZ2h0IjozMDAwfSx7Im1vZHVsZUNvZGUiOiJQcm9tbyIsInBlcm1pc3Npb25Db2RlIjoiQWRtaW4iLCJwZXJtaXNzaW9uV2VpZ2h0IjozMDAwfSx7Im1vZHVsZUNvZGUiOiJQZXJtaXNzaW9uIiwicGVybWlzc2lvbkNvZGUiOiJBZG1pbiIsInBlcm1pc3Npb25XZWlnaHQiOjMwMDB9LHsibW9kdWxlQ29kZSI6IlBlcm1pc3Npb24gVXNlciIsInBlcm1pc3Npb25Db2RlIjoiQWRtaW4iLCJwZXJtaXNzaW9uV2VpZ2h0IjozMDAwfSx7Im1vZHVsZUNvZGUiOiJQZXJtaXNzaW9uIFJvbGUiLCJwZXJtaXNzaW9uQ29kZSI6IkFkbWluIiwicGVybWlzc2lvbldlaWdodCI6MzAwMH0seyJtb2R1bGVDb2RlIjoiQXVkaXQgTG9nIiwicGVybWlzc2lvbkNvZGUiOiJBZG1pbiIsInBlcm1pc3Npb25XZWlnaHQiOjMwMDB9LHsibW9kdWxlQ29kZSI6IkRhdGEgRGljIiwicGVybWlzc2lvbkNvZGUiOiJBZG1pbiIsInBlcm1pc3Npb25XZWlnaHQiOjMwMDB9LHsibW9kdWxlQ29kZSI6IkRhdGEgRGljIFBvbGVzdGFyIiwicGVybWlzc2lvbkNvZGUiOiJBZG1pbiIsInBlcm1pc3Npb25XZWlnaHQiOjMwMDB9LHsibW9kdWxlQ29kZSI6IkRhdGEgRGVhbGVyIENpdHkiLCJwZXJtaXNzaW9uQ29kZSI6IkFkbWluIiwicGVybWlzc2lvbldlaWdodCI6MzAwMH0seyJtb2R1bGVDb2RlIjoiRGF0YSBDb25maWcgQ29udHJvbCIsInBlcm1pc3Npb25Db2RlIjoiQWRtaW4iLCJwZXJtaXNzaW9uV2VpZ2h0IjozMDAwfSx7Im1vZHVsZUNvZGUiOiJEYXRhIFJlZ2lvbiBDb250cm9sIiwicGVybWlzc2lvbkNvZGUiOiJBZG1pbiIsInBlcm1pc3Npb25XZWlnaHQiOjMwMDB9LHsibW9kdWxlQ29kZSI6IkNsYWltIiwicGVybWlzc2lvbkNvZGUiOiJBZG1pbiIsInBlcm1pc3Npb25XZWlnaHQiOjMwMDB9LHsibW9kdWxlQ29kZSI6IkNsYWltIERldGFpbCIsInBlcm1pc3Npb25Db2RlIjoiQWRtaW4iLCJwZXJtaXNzaW9uV2VpZ2h0IjozMDAwfSx7Im1vZHVsZUNvZGUiOiJDbGFpbSBNYW5hZ2VtZW50IiwicGVybWlzc2lvbkNvZGUiOiJBZG1pbiIsInBlcm1pc3Npb25XZWlnaHQiOjMwMDB9LHsibW9kdWxlQ29kZSI6IkNsYWltIENvbnRhY3QiLCJwZXJtaXNzaW9uQ29kZSI6IkFkbWluIiwicGVybWlzc2lvbldlaWdodCI6MzAwMH0seyJtb2R1bGVDb2RlIjoiQ2xhaW0gQ29uZmlnIiwicGVybWlzc2lvbkNvZGUiOiJBZG1pbiIsInBlcm1pc3Npb25XZWlnaHQiOjMwMDB9LHsibW9kdWxlQ29kZSI6IkNsYWltIEltcG9ydCIsInBlcm1pc3Npb25Db2RlIjoiQWRtaW4iLCJwZXJtaXNzaW9uV2VpZ2h0IjozMDAwfSx7Im1vZHVsZUNvZGUiOiJTZXR0aW5nIiwicGVybWlzc2lvbkNvZGUiOiJBZG1pbiIsInBlcm1pc3Npb25XZWlnaHQiOjMwMDB9LHsibW9kdWxlQ29kZSI6IlNldHRpbmcgUmVzZXQgUGFzc3dvcmQiLCJwZXJtaXNzaW9uQ29kZSI6IkFkbWluIiwicGVybWlzc2lvbldlaWdodCI6MzAwMH0seyJtb2R1bGVDb2RlIjoiVmVoaWNsZSIsInBlcm1pc3Npb25Db2RlIjoiQWRtaW4iLCJwZXJtaXNzaW9uV2VpZ2h0IjozMDAwfSx7Im1vZHVsZUNvZGUiOiJWZWhpY2xlIFVzZXIiLCJwZXJtaXNzaW9uQ29kZSI6IkFkbWluIiwicGVybWlzc2lvbldlaWdodCI6MzAwMH0seyJtb2R1bGVDb2RlIjoiQ3VzdG9tZXIiLCJwZXJtaXNzaW9uQ29kZSI6IkFkbWluIiwicGVybWlzc2lvbldlaWdodCI6MzAwMH0seyJtb2R1bGVDb2RlIjoiQ3VzdG9tZXIgVmVoaWNsZSBSZWxhdGlvbnNoaXAiLCJwZXJtaXNzaW9uQ29kZSI6IkFkbWluIiwicGVybWlzc2lvbldlaWdodCI6MzAwMH0seyJtb2R1bGVDb2RlIjoiQ3VzdG9tZXIgSW5mbyIsInBlcm1pc3Npb25Db2RlIjoiQWRtaW4iLCJwZXJtaXNzaW9uV2VpZ2h0IjozMDAwfSx7Im1vZHVsZUNvZGUiOiJQb2ludHMiLCJwZXJtaXNzaW9uQ29kZSI6IkFkbWluIiwicGVybWlzc2lvbldlaWdodCI6MzAwMH0seyJtb2R1bGVDb2RlIjoiUG9pbnRzIFNlcnZpY2UiLCJwZXJtaXNzaW9uQ29kZSI6IkFkbWluIiwicGVybWlzc2lvbldlaWdodCI6MzAwMH0seyJtb2R1bGVDb2RlIjoiUG9pbnRzIFJlcG9ydCBTZXJ2aWNlIiwicGVybWlzc2lvbkNvZGUiOiJBZG1pbiIsInBlcm1pc3Npb25XZWlnaHQiOjMwMDB9LHsibW9kdWxlQ29kZSI6IlZvdWNoZXIiLCJwZXJtaXNzaW9uQ29kZSI6IkFkbWluIiwicGVybWlzc2lvbldlaWdodCI6MzAwMH0seyJtb2R1bGVDb2RlIjoiVm91Y2hlciBUZW1wbGV0ZSIsInBlcm1pc3Npb25Db2RlIjoiQWRtaW4iLCJwZXJtaXNzaW9uV2VpZ2h0IjozMDAwfSx7Im1vZHVsZUNvZGUiOiJWb3VjaGVyIERpc3RyaWJ1dGUiLCJwZXJtaXNzaW9uQ29kZSI6IkFkbWluIiwicGVybWlzc2lvbldlaWdodCI6MzAwMH0seyJtb2R1bGVDb2RlIjoiVm91Y2hlciBEaXN0cmlidXRlIFJlY29yZCIsInBlcm1pc3Npb25Db2RlIjoiQWRtaW4iLCJwZXJtaXNzaW9uV2VpZ2h0IjozMDAwfSx7Im1vZHVsZUNvZGUiOiJGU0FkbWluIiwicGVybWlzc2lvbkNvZGUiOiJBZG1pbiIsInBlcm1pc3Npb25XZWlnaHQiOjMwMDB9LHsibW9kdWxlQ29kZSI6IkZTQWRtaW4gQnVzaW5lc3NDaXR5IiwicGVybWlzc2lvbkNvZGUiOiJBZG1pbiIsInBlcm1pc3Npb25XZWlnaHQiOjMwMDB9LHsibW9kdWxlQ29kZSI6IkZTQWRtaW4gSGFuZG92ZXJDaXR5IiwicGVybWlzc2lvbkNvZGUiOiJBZG1pbiIsInBlcm1pc3Npb25XZWlnaHQiOjMwMDB9LHsibW9kdWxlQ29kZSI6IlJlc2VydmF0aW9uIiwicGVybWlzc2lvbkNvZGUiOiJBZG1pbiIsInBlcm1pc3Npb25XZWlnaHQiOjMwMDB9LHsibW9kdWxlQ29kZSI6IlJlc2VydmF0aW9uIExpc3QiLCJwZXJtaXNzaW9uQ29kZSI6IkFkbWluIiwicGVybWlzc2lvbldlaWdodCI6MzAwMH0seyJtb2R1bGVDb2RlIjoiSGFuZG92ZXIiLCJwZXJtaXNzaW9uQ29kZSI6IkFkbWluIiwicGVybWlzc2lvbldlaWdodCI6MzAwMH0seyJtb2R1bGVDb2RlIjoiSGFuZG92ZXIgRGVsaXZlcnkgVGltZSIsInBlcm1pc3Npb25Db2RlIjoiQWRtaW4iLCJwZXJtaXNzaW9uV2VpZ2h0IjozMDAwfSx7Im1vZHVsZUNvZGUiOiJEYXRhIFByb2plY3QgQWRkcmVzcyIsInBlcm1pc3Npb25Db2RlIjoiQWRtaW4iLCJwZXJtaXNzaW9uV2VpZ2h0IjozMDAwfSx7Im1vZHVsZUNvZGUiOiJOb3RpZmljYXRpb24iLCJwZXJtaXNzaW9uQ29kZSI6IkFkbWluIiwicGVybWlzc2lvbldlaWdodCI6MzAwMH0seyJtb2R1bGVDb2RlIjoiTm90aWZpY2F0aW9uIE1lc3NhZ2UiLCJwZXJtaXNzaW9uQ29kZSI6IkFkbWluIiwicGVybWlzc2lvbldlaWdodCI6MzAwMH0seyJtb2R1bGVDb2RlIjoiTm90aWZpY2F0aW9uIFRlbXBsYXRlIiwicGVybWlzc2lvbkNvZGUiOiJBZG1pbiIsInBlcm1pc3Npb25XZWlnaHQiOjMwMDB9LHsibW9kdWxlQ29kZSI6Ik5vdGlmaWNhdGlvbiBCaXogVHlwZSIsInBlcm1pc3Npb25Db2RlIjoiQWRtaW4iLCJwZXJtaXNzaW9uV2VpZ2h0IjozMDAwfSx7Im1vZHVsZUNvZGUiOiJOb3RpZmljYXRpb24gTWVzc2FnZSBUeXBlIiwicGVybWlzc2lvbkNvZGUiOiJBZG1pbiIsInBlcm1pc3Npb25XZWlnaHQiOjMwMDB9XSwiZXhwaXJlRGF0ZSI6MTY4MDM0MjU2Mjg0OSwidHlwZSI6IlBvcnRhbFVzZXIiLCJpYXQiOjE2ODAxNjk3NjIsImV4cCI6MTY4MDM0MjU2Mn0.UlycipbTqNoifl3XbWLhJFrH1lSctq9n2le3HZsS2AQ' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36' \
  -H 'origin: https://pump-staging.china.polestar.cn' \
  -H 'sec-fetch-site: same-site' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-dest: empty' \
  -H 'referer: https://pump-staging.china.polestar.cn/' \
  -H 'accept-language: zh-CN,zh;q=0.9' \
  --compressed
"""


