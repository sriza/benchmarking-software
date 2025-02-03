import tensorflow as tf

'''
Class that quantizes the given model to be in format as required by the accelerator
'''
class BaseQuantizer:
    def __init__(self):
        self.initializeBaseQuantizer()
    
    def initializeBaseQuantizer():
        pass
        
    def _isQuantizationRequired():
        pass
    
    def quantizeModel():
        # converter = tf.lite.TFLiteConverter.from_keras_model("./models/New/Petals_to_the_Metal-70K_images-trainable_True-MobileNetV2.tflite")
        # converter.optimizations = [tf.lite.Optimize.DEFAULT]
        # converter.inference_input_type = tf.uint8
        # converter.inference_output_type = tf.uint8
        # tflite_model = converter.convert()
        # interpreter = tf.lite.Interpreter(model_path="./models/New/Petals_to_the_Metal-70K_images-trainable_True-MobileNetV2.tflite")
        pass
        