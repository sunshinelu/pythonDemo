# -*- coding: UTF-8 -*-
#visualization3

import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# 设置标题

ax.set_title("Axes Example")
major_ticks = np.arange(0, 101, 20)
minor_ticks = np.arange(0, 101, 5)

# 设置刻度

ax.set_xticks(major_ticks)
ax.set_xticks(minor_ticks, minor=True)
ax.set_yticks(major_ticks)
ax.set_yticks(minor_ticks, minor=True)

# 设置X, Y轴标签

ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")


# 设置网络

ax.grid(which='minor', alpha=0.2)
ax.grid(which='major', alpha=0.5)


# 添加文字

ax.text(42.5, 50, "shiyanlou")

# fig.show()
plt.show()