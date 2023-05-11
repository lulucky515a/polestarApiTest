import os
import sys
import time
import unittest
import unittestreport
from unittestreport import TestRunner

from common import handleWebhook, handleContants, handleHistory
# from common.handleAccount import CreatEmployee


# ------ create account ------
# CreatEmployee()
# CreatEmployee.writeCreateAccount()


suite = unittest.defaultTestLoader.discover(handleContants.testCasesDir,
                                            pattern='test_p*.py')

handleHistory.HandleReportsFile().moveReportFile()

runner = TestRunner(suite,
                    filename=handleContants.path,
                    report_dir=handleContants.reportsDir,
                    title='PoleStarApiTest-个人信息修改',
                    tester='Luke',
                    desc="autoTestApi",
                    templates=1)
runner.run(thread_count=1)

# handleWebhook.testWxWebhook()
