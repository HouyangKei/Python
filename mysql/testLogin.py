'''
Created on 2018年8月21日
test的基础操作
@author: hy
'''
# 导入test驱动:

from datetime import date
from datetime import datetime
import json
from urllib import request
import urllib.request

import pymysql
from pymysql.err import MySQLError
import requests
import web


# 使用 execute()  方法执行 SQL 查询
class login:
    conn = ""
    cur = ""

    def __init__(self):
        # 连接数据库
        self.conn = pymysql.connect(
            host='127.0.0.1', port=3306, user='root', passwd='root', db='test')
        # 游标设置为字典类型  不设置返回元组类型
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 创建表
    def createTable(self):
        sql = """CREATE TABLE python_test (
              live_id INT(11) NOT NULL AUTO_INCREMENT COMMENT '自增主键',
              create_time DATETIME DEFAULT NULL COMMENT '创建时间',
              descp VARCHAR(100) DEFAULT NULL COMMENT '备注',
              PRIMARY KEY (live_id)
            ) ENGINE=INNODB DEFAULT CHARSET=utf8mb4"""
        self.cur.execute(sql)

    # 增加数据
    def add(self, desc):
        # 获取系统时间转为字符串
        # python的%通配符有：%d(整型)，%s（字符型），%f（浮点型）
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql = 'insert into python_test(create_time, descp) values(%s,%s)'
        print(sql)
        try:
            self.cur.execute(sql, [date, desc])
            # 事务提交
            self.conn.commit()
            # 获取新增数据自增ID
            add_id = self.cur.lastrowid
            print("增加数据id为:%d" % add_id)
        except MySQLError as e:
            print("发生异常" + e)
            # 发生异常事务回滚
            self.conn.rollback()

    # 删除
    def delete(self):
        try:
            self.cur.execute("SELECT * FROM python_test")
            liveId = self.cur.fetchone()[0]
            print("id为%d" % liveId)
            sql = "delete from python_test where live_id=%d" % (liveId)
            print(sql)
            self.cur.execute(sql)
            # 事务提交
            self.conn.commit()
            print("删除成功")
        except MySQLError as e:
            print("发生异常" + e)
            # 发生异常事务回滚
            self.conn.rollback()

    # 查询
    def select(self):
        self.cur.execute("SELECT * FROM python_test")
        for r in self.cur.fetchall():
            data = r
            # print(data)
            for i in data:
                print(i + ">>%s" % data[i])

    # 登录
    def login(self, name, pwd):
        sql = "SELECT count(*) as count FROM user where name=%s and pwd=%s "
        num = 0
        try:
            self.cur.execute(sql, [name, pwd])
            # 返回行数
            num = self.cur.fetchone()['count']
            return num
        except MySQLError as e:
            print("发生异常" + e)
            return num

    # 查询
    def selectPythonTest(self):
        data = {}
        try:
            self.cur.execute("SELECT * FROM python_test")
            data = self.cur.fetchall()
            return data
        except MySQLError as e:
            print("发生异常" + e)
            return data

    # 测试(count 计数)
    def test(self):
        sql = "SELECT count(*) as count FROM user"
        try:
            self.cur.execute(sql)
            print(self.cur.fetchone()['count'])

        except MySQLError as e:
            print("发生异常" + e)

    # 关闭数据库连接
    def close(self):
        self.conn.close()


# json 格式化的时候单独处理时间
class DateEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)


# json_1 = {'num': 1112, 'date': datetime.now()}
# print(json.dumps(json_1, cls=DateEncoder))

sql = login()
sql.add("desc9")
# sql.delete()
# sql.selectPythonTest()
sql.close()

