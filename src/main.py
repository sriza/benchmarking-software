import tensorflow as tf
import numpy as np
from PIL import Image
from pycoral.adapters import classify
from pycoral.utils.dataset import read_label_file

import time

try:
    # Convert the model

    # # Save the model
    # with open('model.tflite', 'wb') as f:
    #     f.write(tflite_model)
    
    # Load the TFLite model and allocate tensors.
    interpreter = tf.lite.Interpreter(model_path="./models/MobileNetV1/mobilenet_v1_1.0_224_quant.tflite")
    # /home/sriza/Documents/projects/venv-benchmark/benchmarking-software/models/New/Petals_to_the_Metal-70K_images-trainable_True-MobileNetV2.tflite
    interpreter.allocate_tensors()
    
    labels = read_label_file("./models/MobileNetV1/labels_mobilenet_quant_v1_224.txt")

    # # Get input and output tensors.
    input_details = interpreter.get_input_details()
    # print(input_details)
    output_details = interpreter.get_output_details()
    # print(output_details)
    # print(interpreter.get_signature_list())

    # # Prepare input data (shape must match the model's input shape).
    input_data = np.array(Image.open('./models/MobileNetV1/input/cat.png').convert('RGB').resize((224,224)), dtype=np.uint8)
    # fix the dimension of the input data
    input_data = np.expand_dims(input_data, axis=0)

    # # Set the tensor to point to the input data.
    interpreter.set_tensor(input_details[0]['index'], input_data)

    start = time.perf_counter()
    # # Run the model.
    interpreter.invoke()
    interference_time = time.perf_counter() - start
    # print('inference_time', interference_time)
    
    classes = classify.get_classes(interpreter)
    imgClass = 0
    iam = 0
    
    for c in classes:
        imgClass = max(imgClass,c.score)
        
        if imgClass == c.score:
            iam = labels.get(c.id,c.id)
            # iam = c.id
    
    # print(imgClass, iam)
    # # Get the output data.
    output_data = interpreter.get_tensor(output_details[0]['index'])
    # print(output_data.shape)
except Exception as ex:
    # print('exception occured')
    print('Exception has occurred', repr(ex), ex.__traceback__)