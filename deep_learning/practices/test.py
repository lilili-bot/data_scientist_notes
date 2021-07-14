import os
import sys
import cv2 
import numpy as np
#import matplotlib.pyplot as plt
from tensorflow import keras
from tensorflow.keras.applications import mobilenet_v2
from tensorflow.keras import preprocessing 
from tensorflow.keras.utils import plot_model
from keras_visualizer import visualizer
from IPython.display import SVG
from keras.utils.vis_utils import model_to_dot

# this are the folder names of the things you want to classify
""" classes = ['phone', 'wallet']
# plug in the path to your data folder
base_path = '../data'

data_gen = preprocessing.image.ImageDataGenerator(
    # define the preprocessing function that should be applied to all images
    preprocessing_function=mobilenet_v2.preprocess_input,
    # fill_mode='nearest',
    # rotation_range=20,
    # width_shift_range=0.2,
    # height_shift_range=0.2,
    # horizontal_flip=True, 
    # zoom_range=0.2,
    # shear_range=0.2    
)

train_data_gen = data_gen.flow_from_directory(
        directory=base_path,
        class_mode="categorical",
        classes=classes,
        batch_size=135,
        target_size=(224, 224)
)

xtrain, ytrain = next(train_data_gen)


base_model = mobilenet_v2.MobileNetV2(
    weights='imagenet', 
    alpha=0.35,         # specific parameter of this model, small alpha reduces the number of overall weights
    pooling='avg',      # applies global average pooling to the output of the last conv layer (like a flattening)
    include_top=False,  # we only want to have the base, not the final dense layers 
    input_shape=(224, 224, 3)
)

# freeze it!
base_model.trainable = False


model = keras.Sequential()
model.add(base_model)
model.add(keras.layers.Dense(100, activation='relu'))
model.add(keras.layers.Dropout(0.5))
model.add(keras.layers.Dense(len(classes), activation='softmax'))
model.add(keras.layers.BatchNormalization())
# have a look at the trainable and non-trainable params statistic
model.summary()

model.compile(optimizer=keras.optimizers.Adam(learning_rate=0.001),
              loss=keras.losses.categorical_crossentropy,
              metrics=[keras.metrics.categorical_accuracy])

# observe the validation loss and stop when it does not improve after 3 iterations
callback = keras.callbacks.EarlyStopping(monitor='val_loss', patience=3)

model.fit(xtrain, ytrain, 
          epochs=50, 
          verbose=2,
          batch_size=len(xtrain), 
          callbacks=[callback],
          # use 30% of the data for validation
          validation_split=0.1) """


#model.save('modelses/wallet_phone.h5')


#model = keras.models.load_model('modelses/wallet_phone.h5')

model = mobilenet_v2.MobileNetV2(
    weights='imagenet', 
    alpha=0.35,         # specific parameter of this model, small alpha reduces the number of overall weights
    pooling='avg',      # applies global average pooling to the output of the last conv layer (like a flattening)
    include_top=False,  # we only want to have the base, not the final dense layers 
    input_shape=(224, 224, 3)
)
#plot_model(base_model.generator, to_file='modelG.png', show_shapes=True, show_layer_names=False)
plot_model(model, to_file='model.png')
#plot_model(base_model.combined, to_file='modelComb.png', show_shapes=True, show_layer_names=False)
SVG(model_to_dot(model).create(prog='dot', format='svg'))