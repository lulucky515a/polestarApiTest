# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: handleConfig.py
# @Author: Luke
# @Time: 3月 31, 2023


from configparser import ConfigParser
from common import handleContants


class ReadConfig:

    def __init__(self, filename=handleContants.productConfFile):
        self.config = ConfigParser()
        self.config.read(filename, encoding='utf-8')

    def getValue(self, section, option):
        return self.config.get(section, option)

    def getInt(self, section, option):
        return self.config.getint(section, option)

    def getFloat(self, section, option):
        return self.config.getfloat(section, option)

    def getBoolean(self, section, option):
        return self.config.getboolean(section, option)


conFig = ReadConfig()


class WriteConfig(object):
    @staticmethod
    def writeConfig(datas, filename=handleContants.bpmConfFile):
        if isinstance(datas, dict):
            for value in datas.values():
                if not isinstance(value, dict):
                    return '数据不合法，应为嵌套字典的字典'

            config_write = ConfigParser()
            config_write.read(filenames=handleContants.bpmConfFile, encoding='utf-8')

            for key in datas:
                config_write[key] = datas[key]

            try:
                with open(filename, 'w') as file:
                    config_write.write(file)
                return 'Complete!'
            except Exception as e:
                print('User already exist!')
                raise e
        else:
            return '数据不合法，应为嵌套字典的字典'


bpmFig = ReadConfig(filename=handleContants.bpmConfFile)
writeConfig = WriteConfig()

if __name__ == '__main__':
    res = ReadConfig(filename=handleContants.bpmConfFile)
    res2 = res.getValue('empInfo1', 'employee_number')
    print(res2)

