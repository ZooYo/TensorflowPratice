# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 16:32:43 2017

@author: saop0
"""

import tensorflow as tf

def add_layer(inputs,in_size,out_size,activation_function=None):
    Weights = tf.Variable(tf.random_normal([in_size,out_size]))
    biases = tf.variable(tf.zeros([1,out_size]))+0.1
    Wx_plus_b = tf.matmul(inputs,Weights)+biases
    
    if activation_function is None:
        outputs=Wx_plus_b
    else:
        outputs=activation_function(Wx_plus_b)
    return outputs
        