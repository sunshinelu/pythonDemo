# -*- coding: UTF-8 -*-
#UnderstandingData5－缺失值处理

import pandas as pd

df = pd.read_csv("test_file_nan.csv")

print(df.head(10))
print "=====================我是分割线=========================="

# 查看缺失值
print(df.head(10).isnull())
print "=====================我是分割线=========================="

print(df.head(10).notnull())
print "=====================我是分割线=========================="

# 删除缺失值所在的列或行

print(df.dropna(axis=0)) # axis=0 参数指定行
print "=====================我是分割线=========================="

print(df.dropna(axis=1)) # axis=1 参数指定列

#  填充缺失值
print(df.head(10).fillna(method='pad'))

#  method='bfill' 参数，使用后面的临近值进行填充
print(df.head(10).fillna(method='bfill'))

# 插值填充
print(df.interpolate().head(10))#默认为参数为线性插值，即 method='linear'

'''
除此之外，interpolate()方法还有{‘linear’, ‘time’, ‘index’, ‘values’, ‘nearest’, ‘zero’, ‘slinear’, ‘quadratic’, ‘cubic’, ‘barycentric’, ‘krogh’, ‘polynomial’, ‘spline’, ‘piecewise_polynomial’, ‘from_derivatives’, ‘pchip’, ‘akima’}等插值方法可供选择。

如果你的数据增长速率越来越快，可以选择 method='quadratic'二次插值。
如果数据集呈现出累计分布的样子，推荐选择 method='pchip'。
如果需要填补缺省值，以平滑绘图为目标，推荐选择 method='akima'。
另外，method='akima'，method='barycentric' 和 method='pchip' 需要 Scipy 才能使用。
'''