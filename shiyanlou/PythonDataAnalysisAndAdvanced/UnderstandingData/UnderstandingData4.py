# -*- coding: UTF-8 -*-
#UnderstandingData4－数据预处理


import pandas as pd

df = pd.read_csv("test_file.csv")

# 数据统计
print df.describe()
print "=====================我是分割线=========================="
print "数据总数为："
print df.count()

print "=====================我是分割线=========================="

# 浏览头部数据
print df.head(5)
print "=====================我是分割线=========================="

# 浏览尾部数据
print df.tail(6)
print "=====================我是分割线=========================="

