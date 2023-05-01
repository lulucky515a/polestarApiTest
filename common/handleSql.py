# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: handleSql.py
# @Author: Luke
# @Time: 3月 31, 2023


import psycopg2
import random
from common import conFig


class HandleSql:

    def __init__(self):
        host = conFig.getValue('DataBase', 'host')
        user = conFig.getValue('DataBase', 'user')
        password = conFig.getValue('DataBase', 'password')
        db = conFig.getValue('DataBase', 'db')
        port = conFig.getInt('DataBase', 'port')

        self.conn = psycopg2.connect(host=host, user=user, password=password, database=db, port=port)
        self.cursor = self.conn.cursor()

    def run(self, sql, args=None, is_more=False):
        self.cursor.execute(sql, args=args)
        self.conn.commit()  # 提交查询数据
        #  数据库的隔离性，会造成查询的数据为初始的数据，
        # 1) 解决方法：连接前后断开游标
        # 2) 执行之后提交commit
        if is_more:
            return self.cursor.fetchall()
        else:
            return self.cursor.fetchone()

    def searchSql(self, sql, args=None):
        """
        查询用例结果条数
        :param args:
        :param sql:
        :return:
        """
        self.cursor.execute(sql, args)
        columns = [desc[0] for desc in self.cursor.description]
        results = [dict(zip(columns, row)) for row in self.cursor.fetchall()]
        return results

    def close(self):
        self.cursor.close()
        self.conn.close()

    @staticmethod
    def create_mobile():
        """
        生成随机电话号码
        :return:
        """
        start_mobile = ['138', '139', '188']
        start_mobile = random.choice(start_mobile)
        end_num = ''.join(random.sample('0123456789', 8))

        return start_mobile + end_num

    def is_existed_mobile(self, mobile):
        """
        判断给定的手机号码在数据库中是否存在
        :param mobile: 11位手机号组成的字符串
        :return: True or False
        """
        sql = 'select mobile_phone from member where mobile_phone=%s;'
        if self.run(sql, args=(mobile,)):  # 手机号码已经存在，则返回True，否则返回False
            return True
        else:
            return False

    def create_not_existed_mobile(self):
        """
        随机生成一个在数据库中不存在的手机号码
        :return: 返回一个手机号字符串
        """
        while True:
            one_mobile = self.create_mobile()
            if not self.is_existed_mobile(one_mobile):
                break

        return one_mobile


if __name__ == '__main__':
    mobile = '13816031111'
    sql1 = 'select * from member where mobile_phone=%s'
    sql2 = 'select * from member limit 10'
    ali_list = ['13878534209', '13946053728', '18812508437']

    employee = 'P6200492'
    # sql3 = (f"-- select * from job_adjustment where employee_id=(select id from hr_employee where employee_number='{employee}') order by id desc;")
    sql3 = "select * from job_adjustment where employee_id=(select id from hr_employee where employee_number=%s) order by id desc;"

    do_mysql = HandleSql()
    # res1 = do_mysql.run(sql3, args=(employee,))
    # res1 = do_mysql.searchSql(sql3)[0]["employee_id"]
    # res1 = do_mysql.searchSql(sql3%(employee))#[0]["employee_id"]
    res1 = do_mysql.searchSql(sql3, (employee,))[0]["employee_id"]
    print(res1)
    do_mysql.close()
