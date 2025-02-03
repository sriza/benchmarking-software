import numpy as np
import os.path, random, time
from PIL import Image

import tensorflow as tf
from pycoral.utils.dataset import read_label_file
from pycoral.adapters import classify, detect


class BaseInference:
    def __init__(self, model_path, label_path, input_path):
        self.labels = ''
        self.modelPath = model_path
        self.labelPath = label_path
        self.inputPath = input_path
        pass
    
    def initializeModelInfo(self):
        self.initializeInterpreter()
        self.getInputDetails()
        self.getOutputDetails()
    
    def initializeInterpreter(self):
        self.interpreter = tf.lite.Interpreter(self.modelPath)

        if self.isValidModel():
            self.interpreter.allocate_tensors()
            return True
        
        return False

    def isValidModel(self):
        ops_details = self.interpreter._get_ops_details()

        if "edgetpu" in ops_details[0]['op_name']:
            return False
        return True
    
    def isQuantizationNecessary(self):
        return False
    
    def getLabels(self):
        return read_label_file(self.labelPath)
    
    def getModelSize(self):
        return os.stat(self.modelPath).st_size/(1024*1024)

    def getInputSize(self):
        return self.getInputDetails()[0]["shape"]
    
    def getInputDetails(self):
        return self.interpreter.get_input_details()

    def getOutputDetails(self):
        return self.interpreter.get_output_details()
        
    def setInputData(self):
        imageName = random.choice(os.listdir(self.inputPath))
        imagePath = os.path.join(self.inputPath, imageName)
        dataSize = self.getInputSize()
        input_data = np.array(Image.open(imagePath).convert('RGB').resize((dataSize[1],dataSize[2])), dtype=np.uint8)
        input_data = np.expand_dims(input_data, axis=0)
        self.interpreter.set_tensor(self.getInputDetails()[0]['index'], input_data)

    def classifyTask(self):
        self.setInputData()
        start = time.perf_counter()
        self.interpreter.invoke()
        inference_time = (time.perf_counter() - start)*1000
        
        classes = classify.get_classes(self.interpreter)
        imgClass = 0
        iam = 0
        
        for c in classes:
            imgClass = max(imgClass,c.score)
            
            if imgClass == c.score:
                iam = self.getLabels().get(c.id,c.id)

        return [imgClass , inference_time, iam]

    def detectTask(self):
        self.setInputData()
        start = time.perf_counter()
        self.interpreter.invoke()
        inference_time = time.perf_counter() - start
        classes = detect.get_objects(self.interpreter)
        imgClass = 0
        iam = 0

        for c in classes:
            imgClass = max(imgClass,c.score)

            if imgClass == c.score:
                iam = self.getLabels().get(c.id,c.id)

        return [imgClass,inference_time, iam]
        
    def run(self, task):
        if task == "detect":
            reportParams = self.detectTask()
        elif task == "classify":
            reportParams = self.classifyTask()
        else:
            raise Exception("Invalid model task"+ task)
        return {"accuracy": reportParams[0], "inference_time": reportParams[1], "detectedAs": reportParams[2]}