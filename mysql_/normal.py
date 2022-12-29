#!/usr/bin/python3

import pymysql

# 打开数据库连接
# db = pymysql.connect("192.168.1.133", "root", "123456", "cy_db")
db = pymysql.connect(host='192.168.1.133', user='root', password='123456',db='cy_db')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT * FROM hello")

# 使用 fetchall() 方法获取s所有数据.
data = cursor.fetchall()
sql = "insert into hello value ('1234')"
cursor.execute(sql)
db.commit()

print(data)

# 关闭数据库连接
db.close()
