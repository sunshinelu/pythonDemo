# -*- coding: utf-8 -*-
# purchasesDemo3




import pandas as pd
import numpy as np
from sklearn.externals import joblib

# 使用 Pandas 读取数据
df = pd.read_excel("user_prediction.xlsx", header=0)

# 特征
x = df.iloc[:, 0:8]

# 加载模型
model_GaussianNB = joblib.load('model_GaussianNB.pkl')

# 返回预测概率（%）
results = model_GaussianNB.predict_proba(x) * 100

# 将预测概率转换为 DataFrame
results_df = pd.DataFrame(np.around(results, 2), columns=['非会员概率'.decode('utf-8'), '会员概率'.decode('utf-8')])

# 将预测概率添加到原数据集中最后一列
df_merged = pd.concat([df.drop("用户是否为会员".decode('utf-8'), axis=1), results_df['会员概率'.decode('utf-8')]], axis=1)

# 输出前 20 列
print(df_merged.head(20))