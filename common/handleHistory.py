# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: handleHistory.py
# @Author: Luke
# @Time: 3月 31, 2023


import shutil
import os
from common import reportsDir, historyReportDir


class HandleReportsFile:
    fileNameList = os.listdir(reportsDir)

    def getReportFile(self):
        html_list = [file for file in self.fileNameList if file.endswith(".html")]
        return html_list

    def moveReportFile(self):
        for file in self.getReportFile():
            src = os.path.join(reportsDir, file)
            shutil.move(src=src, dst=historyReportDir)

    @staticmethod
    def getReportFilePath():
        try:
            file = "Report_" + max([i.split("_")[-1].split(".")[0] for i in os.listdir(reportsDir)]) + ".html"
            return file
        except Exception as e:
            raise e


if __name__ == '__main__':
    # HandleReportsFile().move_report_file()
    print(HandleReportsFile().getReportFilePath())
