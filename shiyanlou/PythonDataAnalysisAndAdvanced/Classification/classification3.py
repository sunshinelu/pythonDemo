# -*- coding: UTF-8 -*-
# classification3－SVM


from matplotlib import pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
# 导入支持向量机
from sklearn.svm import SVC

# 导入数据
data = pd.read_csv("two_class_data.csv", header=0)

# 定义特征变量和目标变量
feature = data[['x', 'y']].values
target = data['class'].values

# 对数据集进行切分，70% 为训练集，30% 为测试集。
x_train, x_test, y_train, y_test = train_test_split(feature, target, test_size=0.3, random_state=50)

# 构建模型
model = SVC()

# 训练模型
model.fit(x_train, y_train)

# 预测
results = model.predict(x_test)

# 以默认样式绘制训练数据
plt.scatter(x_train[:, 0], x_train[:, 1], alpha=0.3)

# 以方块样式绘制测试数据
plt.scatter(x_test[:, 0], x_test[:, 1], marker=',', c=y_test)

# 将预测结果用标签样式标注在测试数据左上方
for i, txt in enumerate(results):
    plt.annotate(txt, (x_test[:, 0][i], x_test[:, 1][i]))

plt.show()

