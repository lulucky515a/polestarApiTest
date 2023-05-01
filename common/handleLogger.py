# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: handleLogger.py
# @Author: Luke
# @Time: 3月 31, 2023


import logging
import logging.handlers
from common.handleConfig import conFig
from common import handleContants


inLevel = eval(conFig.getValue('LogNew', 'in_level'))
outLevel = eval(conFig.getValue('LogNew', 'out_level'))
fileOutLevel = eval(conFig.getValue('LogNew', 'file_out_level'))
dataFormatter = conFig.getValue('LogNew', 'fmt')


def getLogger(logger_name):
    """
    :param logger_name: 定义日志输出的名称
    :return:
    """
    logger = logging.getLogger(logger_name)
    logger.setLevel(inLevel)

    fmt = dataFormatter
    formatter = logging.Formatter(fmt)

    file_name = handleContants.logFilename
    file_handler = logging.handlers.RotatingFileHandler(
        file_name, maxBytes=20 * 1024 * 1024, backupCount=10, encoding="utf-8")
    file_handler.setLevel(fileOutLevel)
    file_handler.setFormatter(formatter)

    ch = logging.StreamHandler()
    ch.setLevel(outLevel)
    ch.setFormatter(formatter)

    logger.addHandler(ch)
    logger.addHandler(file_handler)

    return logger


caseLog = getLogger(logger_name='autoTestApi')


if __name__ == '__main__':
    lg = caseLog
    caseLog.error('this is test!!!')