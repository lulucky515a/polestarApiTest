# polestarApiTest
## 项目背景介绍
- 本项目是为了产品发布之后，快速进行CICD

## 项目开发环境
- 开发环境：
  - python3.8
  - pycharm

## 项目框架
- Unittest
  - 自动化测试框架
- unittestreport
  - 测试报告

## 项目启动或者使用说明
- 运行项目脚本
  - main.py
- 更新车辆状态
  - from common import handleData.py
    - 获取系统时间
      - TradeDateTime()
    - 获取unionid
      - get_unionid()
    - 更新车辆订单状态
      - update_order_status()
    - 生成vin
      - create_vin()

- 获取金融方案
  - test_finance.py
- 获取订单信息
  - from common import handleCarInfo.order
- 获取车辆信息
  - from common import handleCarInfo.car_info
- 获取金融订单信息
  - from common improt handleCarInfo.loan_order_detail

## 项目结构简介
- common
  - 封装代码中需要的各种方法
- datas
  - 数据文件配置
- logs
  - 日志文件
- testCases
  - 测试用例文件
- venv
  - 虚拟环境配置
- main.py
  - 主程序入口
- requirements.txt
  - 程序依赖的安装包

## 项目作者
Luke

## 项目更新链接
暂无

## 项目历史版本
参考coding更新记录

## 项目联系方式
zhixiang.lu@supplier.polestar.com