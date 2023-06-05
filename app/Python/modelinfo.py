import numpy as np
import cv2
import tensorflow as tf

# Load the image
image_path = "storage/app/iamges/image.jpg"
image = cv2.imread(image_path)

# Resize the image to 224x224
image = cv2.resize(image, (224, 224))

# Normalize the image
image = image.astype('float32') / 255.0

# Load the TFLite model
model_path = "app/Python/model/VGG16dec.tflite"
interpreter = tf.lite.Interpreter(model_path=model_path)
interpreter.allocate_tensors()

# Get input and output details
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Set input tensor
input_data = np.expand_dims(image, axis=0)
interpreter.set_tensor(input_details[0]['index'], input_data)

# Perform inference
interpreter.invoke()

# Get the output tensor
output_data = interpreter.get_tensor(output_details[0]['index'])

# Print the predicted output
print(output_data)
