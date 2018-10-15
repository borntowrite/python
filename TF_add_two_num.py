import tensorflow as tf

intNum1 = int(input("enter num 1: "))
intNum2 = int(input("enter num 2: "))

num1 = tf.Variable(intNum1)
num2 = tf.Variable(intNum2)

sum = tf.add(num1, num2)

print("sum = " + str(sum))

globalVarsInitializer = tf.global_variables_initializer()

with tf.Session() as sess:
    globalVarsInitializer.run()
    result = sum.eval()

print ("result = " + str(result))

