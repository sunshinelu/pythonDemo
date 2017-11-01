# -*- coding: UTF-8 -*-
# cluster3－绘制k-均值聚类的决策边界


from sklearn.cluster import KMeans
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

# 导入数据
data = pd.read_csv("three_class_data.csv", header=0)

x = data[["x", "y"]]

# 建立模型
model = KMeans(n_clusters=3)
model.fit(x)

# 计算聚类过程中的决策边界
x_min, x_max = data['x'].min() - 1, data['x'].max() + 1
y_min, y_max = data['y'].min() - 1, data['y'].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, .01), np.arange(y_min, y_max, .01))

result = model.predict(np.c_[xx.ravel(), yy.ravel()])

# 将决策边界绘制绘制出来
result = result.reshape(xx.shape)

plt.contourf(xx, yy, result, cmap=plt.cm.Greens)

plt.scatter(data['x'], data['y'], c=model.labels_, s=15)

# 绘制聚类中心点
center = model.cluster_centers_
plt.scatter(center[:, 0], center[:, 1], marker='p', linewidths=2, color='b', edgecolors='w', zorder=20)
plt.show()