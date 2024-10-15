import cv2
import numpy as np
import tensorflow.lite as tflite
from picamera2 import Picamera2
from time import sleep

# Initialize the camera
picam2 = Picamera2()
picam2.start()

# Allow the camera to adjust
sleep(2)

# Load the TensorFlow Lite model
interpreter = tflite.Interpreter(model_path="model.tflite")
interpreter.allocate_tensors()

# Get input and output tensors details
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Capture an image using picamera2
image = picam2.capture_array()

# Preprocess the image for the model
input_shape = input_details[0]["shape"]
resized_image = cv2.resize(image, (input_shape[1], input_shape[2]))
input_data = np.expand_dims(resized_image, axis=0)

# Run inference
interpreter.set_tensor(input_details[0]["index"], input_data)
interpreter.invoke()

# Get the result
output_data = interpreter.get_tensor(output_details[0]["index"])
print("Inference result:", output_data)
