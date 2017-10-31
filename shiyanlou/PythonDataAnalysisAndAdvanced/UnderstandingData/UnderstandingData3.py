# -*- coding: UTF-8 -*-
#UnderstandingData3－链接mysql


import MySQLdb

# 连接数据库
db = MySQLdb.connect(host="localhost", user="root", passwd="", db="shiyanlou")

# 获取操作游标
cur = db.cursor()

# 使用 execute 方法执行 SQL 查询语句
cur.execute("SELECT * FROM person")
3L

# 输出查询
for row in cur.fetchall():
     print row # 注意缩进



# 关闭数据库连接
db.close()