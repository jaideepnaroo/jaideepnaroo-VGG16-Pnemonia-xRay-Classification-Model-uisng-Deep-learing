# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 13:19:41 2022

@author: Jaideep Naroo
"""

from keras.models import load_model
import tensorflow as tf
#from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
#from tensorflow.keras.utils import load_img
#from tensorflow.keras.utils import img_to_array
import numpy as np

model = load_model('model_vgg16.h5')
img = tf.keras.utils.load_img('chest_xray/test/PNEUMONIA/person76_virus_138.jpeg', target_size=(224, 224))
x = tf.keras.utils.img_to_array(img)

x= np.expand_dims(x, axis=0)
img_data = preprocess_input(x)
classes = model.predict(img_data)
