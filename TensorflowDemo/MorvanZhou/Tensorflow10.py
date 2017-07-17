# -*- coding:utf-8 -*-
import tensorflow as tf

"""
https://www.youtube.com/watch?v=FTR36h-LKcY&index=14&list=PLXO45tsB95cKI5AIlf5TxxFPzb-0zeVZ8
添加层:layer1或者layer2


"""
def add_layer(inputs, in_size, out_size, activation_function = None):
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))#Weights中W大写，是因为Weights是一个矩阵
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)#biases首字母小写是因为biases是一个列表
    Wx_plus_b = tf.matmul(inputs, Weights) + biases
    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs