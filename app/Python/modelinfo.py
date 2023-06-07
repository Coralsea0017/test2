import sys
import numpy as np
import cv2
import tensorflow as tf

# Read the image path from command-line arguments
image_path = sys.argv[1]

# Load the image
image = cv2.imread(image_path)

# Rest of the code remains the same...

# Check if the image is successfully loaded
if image is not None:
    # Resize the image to 224x224
    image = cv2.resize(image, (224, 224))

    # Normalize the image
    image = image.astype('float32') / 255.0

    # Load the TFLite model
    model_path = "/home/users/2/deca.jp-broad-hyuga-0115/web/fcdb/app/Python/model/TLVGG16.tflite"
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

    # Load class names
    class_names = ['2194201', '2294201', '2294207']  # Replace with your own class names

    # Find the index of the closest match
    closest_index = np.argmax(output_data)

    # Get the class name of the closest match
    closest_class = class_names[closest_index]

    # Store recognition probability in a separate table or variable
    recognition_probability = output_data[0][closest_index]

    # Print the predicted output
    print(closest_class)
else:
    print("Failed to load the image:", image_path)
