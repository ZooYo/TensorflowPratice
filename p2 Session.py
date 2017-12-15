# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 16:26:20 2017

@author: saop0
"""

import tensorflow as tf

matrix1=tf.constant([[3,3]])
matrix2=tf.constant([[2],
                    [2]])

product=tf.matmul(matrix1,matrix2) #tf.mutiple np.dot(n1,n2)

#method 1
sess=tf.Session()
result=sess.run(product)
print(result)

#method 2
with tf.Session() as sess:
    result2=sess.run(product)
    print(result2)