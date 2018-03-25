#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/18 下午6:30
# @Author  : weitao
# @Site    : 
# @File    : softmaxDemo.py
# @descrip :
# @Software: PyCharm Community Edition

from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("/MINIST_data",one_hot=True)
print(mnist.train.images.shape)
