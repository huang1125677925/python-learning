import tensorflow as tf

a=tf.constant([-1.0,2.0,-100])

with tf.Session() as sess:
	b=tf.nn.relu(a)
	c=tf.nn.softplus(a)
	d=tf.nn.softsign(a)
	print(sess.run(b))
	print(sess.run(c))
	print(sess.run(d))