# -*- coding:utf-8 -*-
import tensorflow as tf
import numpy as np

"""
这节课主要介绍使用tensorflow进行参数优化的例子。
以最简单的线性回归为例。
"""

# create data
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data*0.1 + 0.3
""""
weight: 0.1
biase: 0.3
通过优化找出最优的weight和baise
"""
### create tensorflow structure start ###
Weights = tf.Variable(tf.random_uniform([1], -01.0, 1.0))
biases = tf.Variable(tf.zeros([1]))

y = Weights * x_data + biases

loss = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

init = tf.initialize_all_variables()
### create tensorflow structure end ###

sess = tf.Session()
sess.run(init) # Very important

for step in range(201):
    sess.run(train)
    if step % 20 == 0 :
        print(step, sess.run(Weights), sess.run(biases))