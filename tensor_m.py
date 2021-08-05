import keras
from keras.backend import softmax
from keras.layers import Flatten
from keras.layers.pooling import MaxPooling2D
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import MaxPool2D, Conv2D
from keras.utils import np_utils
import tensorflow as tf
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import pickle
import PIL
import matplotlib.pyplot as plt
#
#d = pd.read_csv('mnist_train.csv')
#label = d['label']
#data = d.drop('label', axis=1)
#data = data.astype('float32')
#
#d = pd.read_csv('mnist_test.csv')
#l = d['label']
#d = d.drop('label', axis=1)
#data = data.astype('float32')
#
#total = data.append(d)
#total_label = label.append(l)
#
#X_train, X_test, y_train, y_test = train_test_split(total.values,total_label.values, test_size=0.2, random_state=50)
#X_train /= 255
#X_test /= 255
#X_train_reshape = np.array(X_train).reshape(X_train.shape[0],28,28,1)
#X_test_reshape = np.array(X_test).reshape(X_test.shape[0],28,28,1)
#
#print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))
#
#model = Sequential()
#model.add(Conv2D(64,(3,3),strides=1, input_shape= X_test_reshape.shape[1:], activation='relu'))
#model.add(MaxPooling2D(pool_size=(2,2),strides=1))
#model.add(Conv2D(64,(3,3),strides=1,activation='relu'))
#model.add(MaxPooling2D(pool_size=(2,2),strides=1))
#model.add(Conv2D(64,(3,3),strides=1,activation='relu'))
#model.add(MaxPooling2D(pool_size=(2,2),strides=1))
#model.add(Flatten())
#model.add(Dense(64, activation='relu'))
#model.add(Dense(32, activation='relu'))
#model.add(Dense(10, activation='softmax'))
#model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
#
#model.summary()
#model.fit(X_train_reshape, y_train, epochs=5,verbose=1,validation_split=0.3)
#
#model.save('CNN_test')



model = tf.keras.models.load_model('CNN_test')
