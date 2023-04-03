# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: getCarType.py
# @Author: Luke
# @Time: 3月 31, 2023


import json

with open("/Users/luzhixiang/PycharmProjects/autoTestApi/datas/car_polestar21.json", "r", encoding="utf-8") as f1:
    car_info = json.loads(f1.read())
# print(car_info)

# 获取pump的order订单信息
# string.replace(configdetail.ModelName,'-','')+'-'+configdetail.ModelYear+filter(configdetail.Summarizes,'Type==Engine')[0].Code
# Polestar2-2024-FE
# filter(car_info["configdetail"]["Summarizes"])
# print(car_info["configdetail"]["ModelName"] + "-" + car_info["configdetail"]["ModelYear"] + "-" + )
# print([i for i in filter(lambda x:x=="Engine", car_info["configdetail"]["Summarizes"])])
model = car_info["configdetail"]["Summarizes"]
model_name = "engine"
model_type = []
# for key in model:
#     if key["Id"] == model_name:
#         model_type.append(key["Code"])
model_type_detail = [key["Code"] for key in model if key["Id"] == model_name]
# print(model_type)
print(f'购买的车型为：{"".join(car_info["configdetail"]["ModelName"].split("-"))}-'
      f'{car_info["configdetail"]["ModelYear"]}-{model_type_detail[0]}')

print(107640+251160)