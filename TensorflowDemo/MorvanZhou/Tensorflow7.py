# -*- coding:utf-8 -*-
import tensorflow as tf

"""
这节课主要介绍Tensorflow中的变量
"""

state = tf.Variable(0, name = 'counter')
print(state.name)
one = tf.constant(1)
print(one)

new_value = tf.add(state, one)
update = tf.assign(state, new_value)

init = tf.initialize_all_variables() # must have if define variable

with tf.Session() as sess:
    sess.run(init)#初始化variable
    for _ in range(3):
        sess.run(update)
        print(sess.run(state))