# encding:utf-8

'''
@author: Hollow
@file: mysql_demo.py
@time: 2019-11-14 10:07

'''

from pymysql import cursors,connect

#连接数据库
conn = connect(host="localhost",
               user='root',
               db='guest',
               password='123456',
               charset='utf8mb4',
               cursorclass='cursors.DictCursor')

# try:
#     with conn.cursor() as cursor:
#         #创建嘉宾表
#