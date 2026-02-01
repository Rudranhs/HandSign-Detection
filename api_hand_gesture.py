from google.colab import files
import os
import tensorflow as tf
assert tf.__version__.startswith('2')

from mediapipe_model_maker import gesture_recognizer

import matplotlib.pyplot as plt

ploaded = files.upload()

from mediapipe_model_maker import gesture_recognizer

# Set paths for the dataset
dataset_path = 'your_dataset_directory_path'

# Load the dataset
data = gesture_recognizer.Dataset.from_folder(dataset_path)

# Split dataset into training and validation
train_data, test_data = data.split(0.8)

# Create and train the gesture recognizer model
model = gesture_recognizer.GestureRecognizer.create(train_data)

# Evaluate the model on test data
loss, accuracy = model.evaluate(test_data)
print(f'Test accuracy: {accuracy}')

# Export the trained model
model.export_model('gesture_recognizer_model')


plt.plot(model.history.history['accuracy'])
plt.plot(model.history.history['val_accuracy'])
plt.title('Model Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend(['train', 'validation'], loc='upper left')
plt.show()


model = tf.keras.models.load_model('gesture_recognizer_model')

# Use this model to classify gestures in real-time
