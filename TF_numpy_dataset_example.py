
from keras.models import Sequential
from keras.layers import Dense
import numpy
from numpy import array

######################################
# Numpy Data Set
# one dimensional example
######################################
# list of data
dataset = numpy.loadtxt("test_array.csv", delimiter=",")
# print(dataset[:,0:9]) # all in y & 9 items from 0 in x
# print(dataset[:,8]) # all in y & dataset[][8]

#dataset = numpy.loadtxt("pima-indians-diabetes.csv", delimiter=",")
x = dataset[:, 0:8]
y = dataset[:, :9]
z = dataset[0:1, 0:1]
x1 = dataset[:, :-1] #all in y, all in x except the last one
x2 = dataset[:, -1] #all in y, the last one only, same as dataset[:, 8]
x3 = dataset[:, 8]
print(y)

# data = array(dataset)
# print("ROW : %d" % data.shape[0])
# print("COL : %d" % data.shape[1])
# print(data.shape)
# data = data.reshape((data.shape[0], data.shape[1], 1))
# print(data.shape)