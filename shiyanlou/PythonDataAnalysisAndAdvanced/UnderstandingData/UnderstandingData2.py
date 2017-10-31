# -*- coding: UTF-8 -*-
#UnderstandingData2－使用Pandas读取文件
# 参考链接：https://pandas.pydata.org/pandas-docs/stable/io.html#

import pandas as pd

# 读取csv文件
df = pd.read_csv("test_file.csv")
print df

print "=============我是分割线==============="

# JSON 文件
pd.read_json

# HTML 文件
pd.read_html

# 本地剪切板
pd.read_clipboard

# MS Excel 文件
pd.read_excel

# HDF5Format 文件
pd.read_hdf

# Feather 格式
pd.read_feather

#Msgpack
pd.read_msgpack

# Stata
pd.read_stata

# SAS
pd.read_sas

# Python Pickle 格式
pd.read_pickle

# SQL 数据库
pd.read_sql

# Google Big Query
pd.read_gbq



# 读取txt格式文件

df2 = pd.read_table("test_file.txt", header=0, sep='\t')
print df2