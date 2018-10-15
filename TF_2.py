import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

a = tf.constant(5)
b = tf.constant(6)
#result = tf.add(a,b)
result = tf.multiply(a,b)
#sess = tf.Session()
#print(sess.run(result))
with tf.Session() as sess:
    output = sess.run(result)
    print(output)

mnist = input_data.read_data_sets("/tmp/data/", one_hot=True)

n_nodes_hl1 = 500
n_nodes_hl2 = 500
n_nodes_hl3 = 500

n_classes = 10
batch_size = 100

# height * width
#x = tf.placeholder(dtype=tf.float32, shape=[None,784])























