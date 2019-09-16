import tensorflow as tf
import numpy as np
'''
为什么算不出来结果，令人费解

'''
x_data=np.linspace(-1,1,300)[:,np.newaxis]
# newaxis 这玩意到底有啥用，https://blog.csdn.net/lanchunhui/article/details/49725065
'''
>> x = np.arange(3)
>> x
array([0, 1, 2])
>> x.shape
(3,)

>> x[:, np.newaxis]
array([[0],
       [1],
       [2]])

>> x[:, None]
array([[0],
       [1],
       [2]])

>> x[:, np.newaxis].shape
 (3, 1)
'''

noise=np.random.normal(0,0.05,x_data.shape)

y_data=np.square(x_data)-0.5+noise

xs=tf.placeholder(tf.float32,[None,1])
ys=tf.placeholder(tf.float32,[None,1])

print(x_data)
print(y_data)
# 构建网络模型

def add_layer(inputs, in_size, out_size, activation_function = None):
	weights=tf.Variable(tf.random_normal([in_size,out_size]))

	biases=tf.Variable(tf.zeros([1,out_size])+0.1)

	Wx_plus_b=tf.matmul(inputs, weights)+biases
	print(weights)
	print(biases)
	print(Wx_plus_b)
	if activation_function is None:
		outputs=Wx_plus_b
	else:
		outputs=activation_function(Wx_plus_b)

	return outputs

# 构建隐藏层

h1=add_layer(xs,1,20,activation_function=tf.nn.relu)

# 构建输出层
prediction=add_layer(h1,20,1,activation_function=None)
# 计算预测值和真实值间的误差
loss=tf.reduce_mean(tf.reduce_sum(tf.square(ys-prediction),reduction_indices = [1]))

train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)


# 训练模型
# 初始化所有变量
init=tf.global_variables_initializer()


with tf.Session() as sess:
	sess.run(init)
	print(sess.run(h1))
	print(sess.run(train_step,feed_dict={xs:x_data,ys:y_data}))



