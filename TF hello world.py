# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 20:57:36 2017

@author: saop0
"""

import tensorflow as tf

a=tf.constant('hello tf')
sess=tf.Session()
print(sess.run(a))