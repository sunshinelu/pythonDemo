# -*- coding: UTF-8 -*-
# classification4－SVM-非线性分类


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.decomposition import PCA


# 导入数据
data = pd.read_csv('zoo.csv', header=0)

# 定义特征变量和目标变量
feature = data.iloc[:, 1:17].values
target = data['type'].values

# 对数据集进行切分，70% 为训练集，30% 为测试集。
x_train, x_test, y_train, y_test = train_test_split(feature, target, test_size=0.3, random_state=50)

# 构建模型
model = SVC()

# 训练模型
model.fit(x_train, y_train)

# 预测
results = model.predict(x_test)

print(model.score(x_test, y_test))
