# -*- coding:utf-8 -*-

"""Softmax."""
# https://classroom.udacity.com/courses/ud730/lessons/6370362152/concepts/63815621490923

scores = [3.0, 1.0, 0.2]

import numpy as np

def softmax(x):
    """Compyte softmax values for each sets for socres in x ."""
    return np.exp(x) / np.sum(np.exp(x), axis=0)

print(softmax(scores))
# print(softmax(scores * 10))
# print(softmax(scores / 10))

# Plot softmax curves
import matplotlib.pyplot as plt
x = np.arange(-2.0, 6.0, 0.1)
scores = np.vstack([x, np.ones_like(x), 0.2 * np.ones_like(x)])

# plt.plot(x, softmax(scores) .T, linewidth=2)
# plt.plot(x, softmax(scores * 10) .T, linewidth=2)
plt.plot(x, softmax(scores / 10) .T, linewidth=2)
plt.show()




