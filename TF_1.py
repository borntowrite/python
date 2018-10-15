import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))

const = tf.constant(2.0, name="const")
# b=tf.Variable(2.0, name='b')
# c=tf.Variable(1.0, name='c')