import tensorflow as tf


a=tf.constant([[-1.0,2.0,3.0,4.0]])

with tf.Session() as sess:

	b=tf.nn.dropout(a,0.5,noise_shape=[1,4])

	print(sess.run(b))

	c = tf.nn.dropout(a, 0.5, noise_shape=[1, 1])

	print(sess.run(c))

