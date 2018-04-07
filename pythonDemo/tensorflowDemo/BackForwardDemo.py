import tensorflow as tf
import numpy as np

# 声明变量。
w1 = tf.Variable(tf.random_normal([2, 3], stddev=1, seed=1))
b1 = tf.Variable(tf.constant(0.0, shape=[3]))
w2 = tf.Variable(tf.random_normal([3, 1], stddev=1, seed=1))
b2 = tf.Variable(tf.constant(0.0, shape=[1]))

# 暂时将输入的特征向量定义为一个常量。注意这里x是一个1*2的矩阵。
#x = tf.constant([[0.7, 0.9]])

##placeholeder
x = tf.placeholder(dtype=tf.float32,shape = [2,2],name = "input")
y = tf.placeholder(dtype=tf.float32,shape = [1,2],name = "output")

# 实现神经网络的前向传播过程，并计算神经网络的输出。
a = tf.nn.relu(tf.matmul(x, w1)+b1)
y_ = tf.nn.relu(tf.matmul(a, w2)+b2)
cross_entropy = -tf.reduce_mean(
    y * tf.log(tf.clip_by_value(y_, 1e-10, 2.0)))
#cross_entropy = tf.nn.sigmoid_cross_entropy_with_logits(labels=y,logits=y_)
# 定义学习率。
learning_rate = 0.001
# 定义反向传播算法来优化神经网络中的参数。
train_step =tf.train.AdamOptimizer(learning_rate).minimize(cross_entropy)

sess = tf.Session()
# 运行变量初始化过程。
init_op = tf.global_variables_initializer()
sess.run(init_op)
# 输出[[3.95757794]]
#print(sess.run(y))
for epoch in range(0,10):
    for batch in range(0,1):
        z,cross_entropy_ = sess.run([y_,cross_entropy],feed_dict={x:[[0.7,0.9],[0.8,0.9]],y:[[1.0,1.1]]})
        print(epoch,z,cross_entropy_)
sess.close()