import tensorflow as tf 

configuration = tf.compat.v1.ConfigProto(device_count={"GPU": 0})
session = tf.compat.v1.Session(config=configuration)

import keras
from tensorflow.keras.applications import MobileNet, ResNet50
from tensorflow.keras.preprocessing.image import img_to_array
from keras.applications.mobilenet import preprocess_input
from keras.preprocessing import image
import numpy as np
import json

def load_model():
	model = MobileNet(weights='imagenet')
	print("Khoi tao model thanh cong")
	return model

def _preprocess_image(path):
	#img_rz = np.resize(img, (224, 224, 3))
	#img_rz = np.resize(img, shape)
	img_rz = image.load_img(path, target_size=(224, 224))
	img_rz = img_to_array(img_rz)
	img_rz = np.expand_dims(img_rz, axis=0)
	return preprocess_input(img_rz)
