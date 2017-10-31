# -*- coding: UTF-8 -*-
#UnderstandingData1－数据文件读取

file = open("test_file.csv","r")

for line in file:
    print line

print "==========我是分割线============"

import xlrd

# 打开文件

file2 = xlrd.open_workbook("test_file.xlsx")

# 按索引读取表

table = file2.sheet_by_index(0)

# 读取每行并打印

for i in range(table.nrows):
    print table.row_values(i)
