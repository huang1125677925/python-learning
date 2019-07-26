import tensorflow as tf

import numpy as np

from tensorflow.examples.tutorials.mnist import input_data

learning_rate =0.01
training_rate=20
batch_size=256
display_step=1

examples_to_show=10

X=tf.placeholder('float',[None,n_input])