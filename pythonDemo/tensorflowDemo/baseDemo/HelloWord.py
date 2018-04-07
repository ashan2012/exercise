#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/31 下午12:27
# @Author  : weitao
# @Site    : 
# @File    : HelloWord.py
# @descrip :
# @Software: PyCharm Community Edition

import tensorflow as tf

# 创建常量
hello = tf.constant('Hello,world!')

# 创建会话
sess = tf.Session()

# 执行
result = sess.run(hello)

# 关闭会话
sess.close()

# 输出结果
print(result)