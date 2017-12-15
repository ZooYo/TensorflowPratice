# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 15:23:05 2017

@author: saop0
"""

import tensorflow as tf
import numpy as np

def add_layer(inputs,in_size,out_size,activation_function=None):
    Weights = tf.Variable(tf.random_normal([in_size,out_size]))
    biases = tf.Variable(tf.zeros([1,out_size]))+0.1
    Wx_plus_b = tf.matmul(inputs,Weights)+biases
    
    if activation_function is None:
        outputs=Wx_plus_b
    else:
        outputs=activation_function(Wx_plus_b)
    return outputs

#real data
x_data = np.linspace(-1,1,300)[:,np.newaxis]
noise = np.random.normal(0,0.05,x_data.shape)
y_data = np.square(x_data)-0.5+noise

#placeholder for inputs
xs = tf.placeholder(tf.float32,[None,1])
ys = tf.placeholder(tf.float32,[None,1])

#add hidden layer
l1 = add_layer(xs,1,10,activation_function=tf.nn.relu)

#add outputdata
prediction = add_layer(l1,10,1,activation_function=None)

#value between prediction and real data
loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys-prediction)
,reduction_indices=[1]))

train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

#important step
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

for i in range(1000):
    #tranning
    sess.run(train_step,feed_dict={xs:x_data,ys:y_data})
    if i%50==0:
        #see improvement
        print(sess.run(loss,feed_dict={xs:x_data,ys:y_data}))










