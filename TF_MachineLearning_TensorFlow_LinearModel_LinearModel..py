# Load Data
# The MNIST data-set is about 12MB and will be downloaded automatically
# if it is not located in the given path
from tensorflow.examples.tutorials.mnist import input_data
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn.metrics import confusion_matrix

print(tf.__version__)
'''Load MNIST data and print some information'''
# in https://github.com/lawlite19/MachineLearning_TensorFlow/blob/master/LinearModel/LinearModel.py
# below one is there but in youtube it's changed to 2nd line and worked well anyway.
# data = input_data.read_data_sets("MNIST_data", one_hot = True)
data = input_data.read_data_sets("data/MNIST", one_hot = True)
#Extracting data/MNIST/train-images-idx3-ubyte.gz
#Extracting data/MNIST/train-labels-idx1-ubyte.gz
#Extracting data/MNIST/t10k-images-idx3-ubyte.gz
#Extracting data/MNIST/t10k-labels-idx1-ubyte.gz

# The MNIST data-set has now been loaded and consist of 70,000 images
# and associated labels (i.e. classifications of the images). The data-set is
# split into 3 mutually exclusive sub-sets. we will only use the training and test-sets
# in this tutorial.

print("Size of: ")
print("- Training-set: \t\t{}".format(len(data.train.labels))) # \t - tab
print("- Test-set: \t\t{}".format(len(data.test.labels))) 
print("- Validation-set: \t\t{}".format(len(data.validation.labels))) # won't use this in this tutorial

#result -- so the total is 70,000
#Size of: 
#- Training-set: 		55000
#- Test-set: 		10000
#- Validation-set: 		5000 

#One-Hot Encoding
print(data.test.labels[0:5, :])
##[[0. 0. 0. 0. 0. 0. 0. 1. 0. 0.]
## [0. 0. 1. 0. 0. 0. 0. 0. 0. 0.]
## [0. 1. 0. 0. 0. 0. 0. 0. 0. 0.]
## [1. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
## [0. 0. 0. 0. 1. 0. 0. 0. 0. 0.]]
data.test.cls = np.array([label.argmax() for label in data.test.labels])  # get the actual value
print(data.test.cls[0:5])
##[7 2 1 0 4]

#Data Dimensions
##the data dimenstions are used in several places in the source-code below. in computer
##programming it is generally best to use variables and constants rather than having to hard-code
##specific numbers every time that number is used. this means the numbers only have to be
##changed in on single place. ideally these would be inferred from the data that has been read,
##but here we just write the numbers.

'''define the images information'''
# MNIST images are 28 pixels in each dimension.
img_size = 28
# Images are stored in one-dimensional arrays of this length.
img_size_flat = img_size * img_size
# Tuple with height and width of images used to reshape arrays.
img_shape = (img_size, img_size)
# Number of classes, one class for each of 10 digits.
num_classes = 10

'''define a funciton to plot 9 images'''
# Helper-function for plotting images
# function used to plot 9 images in a 3x3 grid, and writing the true and predicted classes below each image.
def plot_images(images, cls_true, cls_pred=None):
    '''
    @parameter images:   the images info
    @parameter cls_true: the true value of image
    @parameter cls_pred: the prediction value, default is None
    '''
    assert len(images) == len(cls_true) == 9
    fig, axes = plt.subplots(3,3)
    fig.subplots_adjust(hspace=0.3, wspace=0.3)
    for i, ax in enumerate(axes.flat):
        ax.imshow(images[i].reshape(img_shape), cmap='binary')
        # show the true and pred values
        if cls_pred is None:
            xlabel = "True: {0}".format(cls_true[i])
        else:
            xlabel = "True: {0}, Pred {1}".format(cls_true[i], cls_pred[i])
        ax.set_xlabel(xlabel)
        ax.set_xticks([])
        ax.set_yticks([])

'''show 9 images'''
# plot a few images to see if data is correct
# get the first 10 images from the test-set
images = data.test.images[0:9]
# get the true classes for those images.
cls_true = data.test.cls[0:9]
# plot the images and labels using our helper-function above.
plot_images(images=images, cls_true=cls_true)

##7                    2                      1
##true:7           true: 2             true: 1
##0                    4                      1
##true:0           true: 4             true: 1
##4                    9                      5
##true:4           true: 9             true: 5

'''define the placeholder'''
# TensorFlow Graph
# Placeholder variables
x = tf.placeholder(tf.float32, [None, img_size_flat])
y_true = tf.placeholder(tf.float32, [None, num_classes])
y_true_cls = tf.placeholder(tf.int64, [None])

'''define weights and biases'''
# Variables to be optimized
weights = tf.Variable(tf.zeros([img_size_flat, num_classes]))
biases = tf.Variable(tf.zeros([num_classes]))

'''define the model'''
# Model
logits = tf.matmul(x, weights) + biases
y_pred = tf.nn.softmax(logits)
y_pred_cls = tf.argmax(y_pred, dimension=1)
# Cost-function to be optimized
cross_entropy = tf.nn.softmax_cross_entropy_with_logits(logits = logits, labels = y_true)
cost = tf.reduce_mean(cross_entropy)

'''define the optimizer'''
# Optimization method
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.5).minimize(cost)

'''define the accuracy'''
# Performance measures
correct_prediction = tf.equal(y_pred_cls, y_true_cls)
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

'''run the datagraph and use batch gradient descent'''
# Create TensorFlow session
session = tf.Session()
# Initialize variables
#session.run(tf.initialize_all_variables()) # this is old and replaced with below 
session.run(tf.global_variables_initializer())
# Helper-function to perform optimization iterations
batch_size = 100

'''define a function to run the optimizer'''
def optimize(num_iterations):
    '''
    @parameter num_iterations: the traning times
    '''
    for i in range(num_iterations):
        # get a batch of training examples.
        # x_batch now holds a batch of images and
        # y_true_batch are the true labels for those images.
        x_batch, y_true_batch = data.train.next_batch(batch_size)

        # put the batch into a dict with the proper names
        # for placeholder variables in the TensorFlow graph.
        # Note that the place holder for y_true_cls is not set
        # because it is not used during training.
        feed_dict_train = {x: x_batch, y_true: y_true_batch}

        # run the optimizer using this batch of training data.
        # TensorFlow assignes the variables in feed_dict_train
        # to the placeholder variables and then runs the optimizer.
        session.run(optimizer, feed_dict=feed_dict_train)

# helper-function to show performance

feed_dict_test = {x: data.test.images, y_true: data.test.labels, y_true_cls: data.test.cls}

'''define a function to print the accuracy'''    
def print_accuracy():
    # Use TensorFlow to compute the accuracy.
    acc = session.run(accuracy, feed_dict=feed_dict_test)
    print("Accuracy on test-set: {0:.1%}".format(acc))

'''define a function to printand plot the confusion matrix using scikit-learn.''' 
def print_confusion_matrix():
    # get the true classifications for the test-set
    cls_true = data.test.cls

    # get the predicted classifications for the test-set
    cls_pred = session.run(y_pred_cls, feed_dict=feed_dict_test)

    # get the confusion matrix using sklearn
    cm = confusion_matrix(y_true=cls_true, y_pred=cls_pred)

    # print the confusion matrix as text
    print(cm)

    # plot the confusion matrix as an image
    plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)

    # Make various adjustments to the plot.
    plt.tight_layout()
    plt.colorbar()
    tick_marks = np.arange(num_classes)
    plt.xticks(tick_marks, range(num_classes))
    plt.yticks(tick_marks, range(num_classes))
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.show()

'''define a function to plot the error prediciton'''
def plot_example_errors():
    correct, cls_pred = session.run([correct_prediction, y_pred_cls], feed_dict=feed_dict_test)
    incorrect = (correct == False)
    # get the prediction error images
    images = data.test.images[incorrect]
    # get prediction value
    cls_pred = cls_pred[incorrect]
    # get true value
    cls_true = data.test.cls[incorrect]
    plot_images(images[0:9], cls_true[0:9], cls_pred[0:9])

'''define a fucntion to plot weights'''
def plot_weights():
    w = session.run(weights)
    w_min = np.min(w)
    w_max = np.max(w)
    fig, axes = plt.subplots(3, 4)
    fig.subplots_adjust(0.3, 0.3)
    for i, ax in enumerate(axes.flat):
        if i<10:
            image = w[:,i].reshape(img_shape)
            ax.set_xlabel("Weights: {0}".format(i))
            ax.imshow(image, vmin=w_min,vmax=w_max,cmap="seismic")
        ax.set_xticks([])
        ax.set_yticks([])
    plt.show()

if __name__ == "__main__":
    optimize(num_iterations=100)
    print_accuracy()
    plot_example_errors()
    plot_weights()
    print_confusion_matrix()



























