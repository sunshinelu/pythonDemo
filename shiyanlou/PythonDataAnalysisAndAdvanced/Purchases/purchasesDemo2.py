# -*- coding: utf-8 -*-
# purchasesDemo2


import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.externals import joblib

# 使用 Pandas 读取数据
df = pd.read_excel("user_fit.xlsx", header=0)

# 特征
x = df.iloc[:, 0:8]
print df.head(5)

# 目标
y = df['用户是否为会员'.decode('utf-8')]

# 构建高斯贝叶斯分类器
model_GaussianNB = GaussianNB()

# 使用训练集训练模型
model_GaussianNB.fit(x, y)

# 保存模型
joblib.dump(model_GaussianNB, 'model_GaussianNB.pkl')

print('done.')