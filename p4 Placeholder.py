# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 15:55:44 2017

@author: saop0
"""

import tensorflow as tf

input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)

output= tf.multiply(input1,input2)

with tf.Session() as sess:
    print(sess.run(output,feed_dict={input1:[7.0],input2:[2.0]}))