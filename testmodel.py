import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model  # type: ignore
import keras

# print(keras_version)
# print(tf.__version__)
# print("TensorFlow version:", tf.__version__)
# print("Keras version:", keras.__version__)
model = load_model("model\model.h5")
print(model.predict([[3], [5]]))
