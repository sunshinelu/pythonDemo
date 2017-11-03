# -*- coding: utf-8 -*-
# purchasesDemo4


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

# 使用 Pandas 读取数据
df = pd.read_excel("user_fit.xlsx", header=0)

# 特征
x = df.iloc[:, 0:8]

# 目标
y = df['用户是否为会员'.decode('utf-8')]

# 安装 3:7 切分验证集和训练集
train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.3)

# 构建神经网络分类器

model_MLPClassifier= MLPClassifier(activation='logistic',max_iter=50,hidden_layer_sizes=(50,50,50))

# 使用训练集训练模型
model_MLPClassifier.fit(train_x, train_y)

# 使用验证集评估准确度
score_trainset = model_MLPClassifier.score(train_x, train_y)*100
score_testset = model_MLPClassifier.score(test_x, test_y)*100

print("训练集预测准确率: %.2f%%" % score_trainset)
print("测试集预测准确率: %.2f%%" % score_testset)