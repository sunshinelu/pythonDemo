# -*- coding: UTF-8 -*-
# cluster4－聚类方法对比

from sklearn import cluster
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import time

# 导入数据
data = pd.read_csv("three_class_data.csv", header=0)

x = data[["x", "y"]]

# 对聚类方法依次命名
cluster_names = ['KMeans', 'MiniBatchKMeans', 'AffinityPropagation', 'MeanShift', 'SpectralClustering', 'AgglomerativeClustering', 'Birch', 'DBSCAN']

# 确定聚类方法相应参数
cluster_estimators = [
    cluster.KMeans(n_clusters=3),
    cluster.MiniBatchKMeans(n_clusters=3),
    cluster.AffinityPropagation(),
    cluster.MeanShift(),
    cluster.SpectralClustering(n_clusters=3),
    cluster.AgglomerativeClustering(n_clusters=3),
    cluster.Birch(n_clusters=3),
    cluster.DBSCAN()
]

# 为绘制子图准备
plot_num = 1

# 依次运行不同的聚类方法
for name, model in zip(cluster_names, cluster_estimators):

    tic = time.time()

    # 建立模型
    model.fit(x)

    # 绘制子图
    plt.subplot(2, len(cluster_estimators) / 2, plot_num)

    # 计算聚类过程中的决策边界
    x_min, x_max = data['x'].min() - 1, data['x'].max() + 1
    y_min, y_max = data['y'].min() - 1, data['y'].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, .01), np.arange(y_min, y_max, .01))

    if hasattr(model, 'predict'):
        result = model.predict(np.c_[xx.ravel(), yy.ravel()])

        # 将决策边界绘制绘制出来
        result = result.reshape(xx.shape)

        plt.contourf(xx, yy, result, cmap=plt.cm.Greens)

    plt.scatter(data['x'], data['y'], c=model.labels_, s=15)

    # 判断方法中是否由 cluster_centers_ 聚类中心参数，并执行不同的命令
    if hasattr(model, 'cluster_centers_'):
        center = model.cluster_centers_
        plt.scatter(center[:, 0], center[:, 1], marker='p', linewidths=2, color='b', edgecolors='w', zorder=20)

    # 计算算法运行时间
    toc = time.time()
    cluster_time = (toc - tic)*1000

    # 绘图
    plt.title(str(name) + ", " + str(int(cluster_time)) + "ms")
    plot_num += 1

plt.show()