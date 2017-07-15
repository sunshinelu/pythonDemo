# -*- coding: utf-8 -*-
"""
查看tensorflow的版本
查看python的版本
"""

import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))

a = tf.constant(10)
b= tf.constant(32)
print(sess.run(a+b))

print(tf.__version__)

import sys
print(sys.version)