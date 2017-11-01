# -*- coding: utf-8 -*-

import numpy as np
from sklearn.externals import joblib
from sklearn.svm import SVC

# 导入词向量为训练特征
x = np.load('data_09/data/x_train_vec.npy')

# 导入情绪分类作为目标特征
y = np.load('data_09/data/y_train.npy')

# 构建支持向量机分类模型
model = SVC(kernel='rbf', verbose=True)

# 训练模型
model.fit(x, y)

# 保存模型为二进制文件
joblib.dump(model, 'data_09/data/svm_model.pkl')

from sklearn.model_selection import cross_val_score

# 输出模型交叉验证准确率
print(cross_val_score(model, x, y))