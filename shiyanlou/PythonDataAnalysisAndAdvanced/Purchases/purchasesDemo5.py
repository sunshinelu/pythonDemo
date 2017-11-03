# -*- coding: utf-8 -*-
# purchasesDemo5

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

# 使用 Pandas 读取数据
df = pd.read_excel("user_fit.xlsx", header=0, encoding="utf-8")

# 训练特征
x = df.iloc[:, 0:8]

# 训练目标
y = df['用户是否为会员'.decode('utf-8')]

# 读取预测数据
df_pre = pd.read_excel("user_prediction.xlsx", header=0)

# 预测特征
predict_x = df_pre.iloc[:, 0:8]

# 构建模型
model_MLPClassifier= MLPClassifier(activation='logistic',max_iter=50,hidden_layer_sizes=(50,50,50))

# 使用训练集训练模型
model_MLPClassifier.fit(x, y)

# 返回预测概率（%）
results = model_MLPClassifier.predict_proba(predict_x) * 100

# 将预测概率转换为 DataFrame
results_df = pd.DataFrame(np.around(results, 2), columns=['非会员概率'.decode('utf-8'), '会员概率'.decode('utf-8')])

# 将预测概率添加到原数据集中最后一列
df_merged = pd.concat([df_pre.drop("用户是否为会员".decode('utf-8'), axis=1), results_df['会员概率'.decode('utf-8')]], axis=1)

# 按会员概率降排序，并输出前 20 列
print(df_merged.sort_values(by='会员概率'.decode('utf-8'),ascending=False).head(20))

