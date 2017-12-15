# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 16:37:16 2017

@author: saop0
"""

import tensorflow as tf

state = tf.Variable(0,name='Counter')
print(state.name)
one = tf.constant(1)

new_value = tf.add(state,one)
update = tf.assign(state,new_value)

init=tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for _ in range(5):
        sess.run(update)
        print(sess.run(state))
    