#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/18 下午2:27
# @Author  : weitao
# @Site    : 
# @File    : base1-1.py
# @descrip :
# @Software: PyCharm Community Edition

import tensorflow as tf
import numpy as np

b = tf.Variable(tf.zeros([3]))
w = tf.Variable(tf.random_uniform([3,1],-1,1))
x = tf.placeholder(np.float32,name="x")
relu = tf.nn.relu(tf.matmul(w,x)+b)
c = []

init_op = tf.local_variables_initializer()


s = tf.InteractiveSession()
for step in range(0,10):
    input = np.array([1,0,2.0],np.float32)
    result = s.run(init_op,feed_dict={x:input})
    print(step,c,w)