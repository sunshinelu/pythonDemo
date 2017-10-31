# -*- coding: UTF-8 -*-
# classification1－感知机分类模型-查看数据


from matplotlib import pyplot as plt
import pandas as pd


# 读取数据
data = pd.read_csv("two_class_data.csv", header=0)

# 读取数据列
x = data['x']
y = data['y']
c = data['class']

# 绘制散点图，c 参数用于分类着色
plt.scatter(x, y, c=c)
plt.show()