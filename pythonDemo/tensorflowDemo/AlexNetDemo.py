#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/18 下午6:30
# @Author  : weitao
# @Site    :
# @File    : CNNNewDemo.py
# @descrip :  alexNet 2012冠军，主要使用了一些tricks，8层网络，引领了深度学习
# @Software: PyCharm Community Edition

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import numpy as np

import time

import sys;
sys.path.append("/Users/weitao/OpenSource/models/tutorials/image/cifar10")
import cifar10,cifar10_input