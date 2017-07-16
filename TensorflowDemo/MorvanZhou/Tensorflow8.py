# -*- coding:utf-8 -*-
import tensorflow as tf

"""
这节课主要介绍Tensorflow中的placeholder
在一开始的时候hold住变量，从外界传入变量
"""

input1 = tf.placeholder(tf.float32)#type: tf.float32   tensorflow只能处理float32的数据类型
input2 = tf.placeholder(tf.float32)

output = tf.multiply(input1, input2)

with tf.Session() as sess:
    print(sess.run(output, feed_dict={input1:[7.], input2:[2.]}))
