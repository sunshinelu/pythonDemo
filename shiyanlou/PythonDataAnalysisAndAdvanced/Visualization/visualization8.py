# -*- coding: UTF-8 -*-
#visualization8－箱线图

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

# 产生50个小于100的随机数
spread = np.random.rand(50) * 100
print "spread is: "
print spread

# 产生25个值为50的数据
center = np.ones(25) * 50
print "center is: "
print center

# 异常值
outliner_high = np.random.rand(10) * 100 + 100
outliner_low = np.random.rand(10) * -100
data = np.concatenate((spread, center, outliner_high, outliner_low), 0)
ax.boxplot(data)
fig.show()
plt.show()