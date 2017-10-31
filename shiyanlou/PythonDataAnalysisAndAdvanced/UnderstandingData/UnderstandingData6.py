# -*- coding: UTF-8 -*-
#UnderstandingData6－One-Hot Encoding

import pandas as pd

df = pd.read_csv("one_hot_demo.csv", header=0)

# One-Hot Encoding
oneHot = pd.get_dummies(df[['status', 'color']])
oneHot.head(10)

# 重复值处理

print(pd.DataFrame.duplicated(df).head(10))

# 返回一个去重后的数据集
print(pd.DataFrame.drop_duplicates(df))
