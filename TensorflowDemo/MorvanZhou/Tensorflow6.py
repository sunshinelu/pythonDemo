# -*- coding:utf-8 -*-
import tensorflow as tf
"""
这节课主要介绍session的两种打开模式
"""

matrix1 = tf.constant([[3,3]])
matrix2 = tf.constant([[2],
                       [2]])
product = tf.matmul(matrix1, matrix2) # matrix multiply np.dot(m1, m2)

"""
## method 1
sess = tf.Session()
result = sess.run(product)
print(result)
sess.close()
"""


## method 2 不用管sess.close
with tf.Session() as sess:
    result2 = sess.run(product)
    print(result2)