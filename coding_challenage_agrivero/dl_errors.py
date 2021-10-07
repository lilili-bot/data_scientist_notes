import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dropout, Dense, Flatten


IMG_SHAPE = (224, 224, 3)
IMG_SIZE = (IMG_SHAPE[0], IMG_SHAPE[1])
batch_size = 16
num_classes = 3


def get_paths():
    # Let's assume that this function returns a list of tuples of (path_to_img, class_label) sorted by class_label
    pass


def load_data(path, image_size, augment, batch_size):
    # Assume that this function returns a tf dataset object.
    # Images are resized to image_size, normalized between 0 and 1 and bundled to batches of batch_size.
    # If augment = True, data augmentation is applied.
    pass


paths = get_paths()
val_split = 0.2
num_samples = len(paths)
val_path = paths[:val_split * num_samples]
train_path = paths[:(1 - val_split) * num_samples]

train_loader = load_data(train_path, image_size=IMG_SIZE, augment=True, batch_size=batch_size)
val_loader = load_data(val_path, image_size=IMG_SIZE, augment=True, batch_size=batch_size)

# Do transfer learning from VGG
model_vgg16 = tf.keras.applications.vgg16.VGG16(
    include_top=False, weights='imagenet', input_shape=IMG_SIZE)
x = Flatten()(model_vgg16.output)
x = Dense(512, activation='relu')(x)
x = Dropout(0.5)(x)
x = Dense(256, activation='relu')(x)
predictions = Dense(num_classes, activation='sigmoid')(x)
model = Model(inputs=model_vgg16.input, outputs=predictions)
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['sparse_categorical_accuracy'])
history = model.fit(train_loader,
                    steps_per_epoch=len(train_path) * batch_size,
                    batch_size=batch_size,
                    epochs=50,
                    validation_data=val_loader,
                    validation_steps=len(val_path) * batch_size)
