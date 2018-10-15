import tensorflow as tf 
import numpy as np
# print(tf.get_default_graph())
# g1 = tf.Graph()
# g2 = tf.constant(5)
# print(g2.graph is tf.get_default_graph())
# print(g2.graph is g1)

# with g1.as_default():
# 	print(g1 is tf.get_default_graph())

# a = tf.constant(5)
# b = tf.constant(2)
# c = tf.constant(3)

# d = tf.multiply(a,b)
# e = tf.add(c,b)
# f = tf.subtract(d,e)

# fetches = [a,b,c,d,e,f]

# with tf.Session() as sess:
# 	out = sess.run(fetches)

# print(out)
# print(type(out[0]))

# g = tf.constant(4.0, dtype=tf.float64)
# print(g)
# print(g.dtype)

# x = tf.constant([1,2,3], name='x', dtype=tf.float32)
# print(x.dtype)
# x = tf.cast(x, tf.int64)
# print(x.dtype)

# x = tf.constant([[1,2,3],[4,5,6]], dtype=tf.float32)
# print(x.get_shape())
# x = tf.constant(np.array([[[1,2,3],[4,5,6]], [[7,8,9],[10,11,12]]]), dtype=tf.float32)
# print(x.get_shape())

# sess = tf.InteractiveSession()
# c = tf.linspace(0.0, 4.0, 5)
# print("The content of 'c':\n {}\n".format(c.eval()))
# sess.close()

x1 = tf.constant([[1,2,3], [4,5,6], [7,8,9]], dtype=tf.float32)
print(x1.get_shape())
x2 = tf.constant([[1,2,3], [4,5,6]], dtype=tf.float32)
print(x2.get_shape())

expanded_x1 = tf.expand_dims(x1, 0)
print(expanded_x1.get_shape())
expanded_x2 = tf.expand_dims(x2, 2)
print(expanded_x2.get_shape())
result = tf.matmul(expanded_x1,expanded_x2)

with tf.Session() as sess:
	y1 = sess.run(expanded_x1)
	y2 = sess.run(expanded_x2)
	y = sess.run(result)

print(y1)
print(y2)
print(y)












