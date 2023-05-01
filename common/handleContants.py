# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: handleContants.py
# @Author: Luke
# @Time: 3月 31, 2023


import os
import time
from datetime import datetime


def nowDate():
    time_now = datetime.now().strftime("%Y-%m-%d")
    return time_now


now = nowDate()

baseDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

commonDir = os.path.join(baseDir, "common")

confDir = os.path.join(baseDir, "conf")
globalApiConfFile = os.path.join(confDir, "global.conf")
productConfFile = os.path.join(confDir, "product.conf")
sandboxConfFile = os.path.join(confDir, "sandbox.conf")
bpmConfFile = os.path.join(confDir, "bpm.conf")

dataDir = os.path.join(baseDir, "datas")
productExcelFile = os.path.join(dataDir, "bpmPr.xlsx")
sandboxExcelFile = os.path.join(dataDir, "sandbox.xlsx")
pAccountBody = os.path.join(dataDir, "accountBody.json")

empBody = os.path.join(dataDir, "emp.json")
empNullBody = os.path.join(dataDir, "empNull.json")
empListNullBody = os.path.join(dataDir, "empListNull.json")

transferEmpBody = os.path.join(dataDir, "transferEmp.json")
transferEmpNullBody = os.path.join(dataDir, "transferEmpNull.json")

updateEmpBody = os.path.join(dataDir, "updateEmp.json")
updateEmpNullBody = os.path.join(dataDir, "updateEmpNull.json")

logDir = os.path.join(baseDir, "logs")

logName = logDir + '/' + now
if not os.path.exists(logName):
    os.mkdir(logName)

t = datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")  # t的格式是 年月日
logFilename = logName + '/' + "{}.log".format(t)

reportsDir = os.path.join(baseDir, "reports")
historyReportDir = os.path.join(reportsDir, "historyReports")
if not os.path.exists(historyReportDir):
    os.mkdir(historyReportDir)

testApiUnittestReportFile = os.path.join(reportsDir, "testApiUnittestReport.py")
now = time.strftime('%Y%m%d%H%M')
path = os.path.join(reportsDir, "Report" + "_" + now + '.html')

testCasesDir = os.path.join(baseDir, "testCases")
