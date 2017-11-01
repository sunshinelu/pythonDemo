# -*- coding: UTF-8 -*-
# cluster2－k=3

from sklearn.cluster import k_means
from matplotlib import pyplot as plt
import pandas as pd

# 导入数据
data = pd.read_csv("three_class_data.csv", header=0)

x = data[["x", "y"]]

# 建立模型
model = k_means(x, n_clusters=3)

# 绘图
plt.scatter(data['x'], data['y'], c=model[1])
plt.show()