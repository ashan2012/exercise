#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/18 下午6:30
# @Author  : weitao
# @Site    :
# @File    : autoCodeDemo.py
# @descrip :
# @Software: PyCharm Community Edition

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import numpy as np
import sklearn.preprocessing as prep

mnist = input_data.read_data_sets("MNIST_data",one_hot=True)

sess = tf.InteractiveSession()
in_unit = 784
h1_unit = 300
w1 = tf.Variable(tf.truncated_normal([in_unit,h1_unit],stddev = 0.1))
b1 = tf.Variable(tf.zeros([h1_unit]))
w2 = tf.Variable(tf.zeros([h1_unit,10]))
b2 = tf.Variable(tf.zeros([10]))

x = tf.placeholder(dtype=tf.float32,shape = [None,in_unit])
keep_pro = tf.placeholder(tf.float32)
hidden1 = tf.nn.relu(tf.matmul(x,w1)+b1)
hidden1_keep = tf.nn.dropout(hidden1,keep_prob=keep_pro)
y = tf.nn.softmax(tf.matmul(hidden1_keep,w2)+b2)

y_ = tf.placeholder(dtype=tf.float32,shape = [None,10])

cross_entroy = tf.reduce_mean(-tf.reduce_sum(y_*tf.log(y),reduction_indices=[1]))
train_step = tf.train.AdadeltaOptimizer(0.3).minimize(cross_entroy)

tf.global_variables_initializer().run()
correct_prediction = tf.equal(tf.arg_max(y, 1), tf.arg_max(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
for i in range(5000):
    batch_xs,batch_ys = mnist.train.next_batch(100)
    train_step.run({x:batch_xs,y_:batch_ys,keep_pro:0.75})
    if i %100 == 0:
        print(i,"accuracy:",accuracy.eval({x:mnist.test.images,y_:mnist.test.labels,keep_pro:1.0}))

# correct_prediction = tf.equal(tf.arg_max(y,1),tf.arg_max(y_,1))
# accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
print("final:",accuracy.eval({x:mnist.test.images,y_:mnist.test.labels,keep_pro:1.0}))