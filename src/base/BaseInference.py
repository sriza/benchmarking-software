import tensorflow as tf
from src.base.BaseMetrics import BaseMetrics
import numpy as np
from PIL import Image
from pycoral.utils.dataset import read_label_file
from pycoral.adapters import classify
import os.path

class BaseInference:
    def __init__(self, model_path, label_path, input_path):
        self.labels = ''
        self.modelPath = model_path
        self.labelPath = label_path
        self.inputPath = input_path
        self.initializeModalInfo()
        pass
    
    def initializeModalInfo(self):
        print("Interference parameters initialized")
        self.interpreter = tf.lite.Interpreter(self.modelPath)
        self.interpreter.allocate_tensors()
        
        self.metrics = BaseMetrics()
        print("Interference parameters initialized")
        self.getInputDetails()
        print("Interference parameters initialized")
        self.getOutputDetails()
        print("Interference parameters initialized")
        self.setInputData()
        print("Interference parameters initialized")
    
    def isQuantizationNecessary(self):
        # if self.inputDetails():
        print(self.getInputDetails())
        # return False
    
    def getLabels(self):
        return read_label_file(self.labelPath)
    
    def getModalSize(self, file_name):
        pass
    
    def getInputDetails(self):
        return self.interpreter.get_input_details()

    def getOutputDetails(self):
        return self.interpreter.get_output_details()
        
    def setInputData(self):
        inputFiles = os.listdir(self.inputPath)
        imagePath = os.path.join(self.inputPath, inputFiles[0])
        input_data = np.array(Image.open(imagePath).convert('RGB').resize((224,224)), dtype=np.uint8)
        # input_data = np.array(Image.open('./models/MobileNetV1/input/cat.png').convert('RGB').resize((224,224)), dtype=np.uint8)
        # fix the dimension of the input data
        input_data = np.expand_dims(input_data, axis=0)
        self.interpreter.set_tensor(self.getInputDetails()[0]['index'], input_data)
        
    def run(self):
        # start = time.perf_counter()
        # # Run the model.
        self.interpreter.invoke()
        # self.interference_time = time.perf_counter() - start
        # print('inference_time', interference_time)
        
        classes = classify.get_classes(self.interpreter)
        imgClass = 0
        iam = 0
        
        for c in classes:
            imgClass = max(imgClass,c.score)
            
            if imgClass == c.score:
                iam = self.getLabels().get(c.id,c.id)
                # iam = c.id
        
        print(imgClass, iam)
        # # Get the output data.
        output_data = self.interpreter.get_tensor(self.getOutputDetails()[0]['index'])
        print(output_data.shape)
        pass
        
        
    
    
        
        
    
    