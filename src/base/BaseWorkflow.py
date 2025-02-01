from src.base.BaseConfig import BaseConfig
from src.base.BaseInference import BaseInference
from src.base.BaseReport import BaseReport
from src.base.BaseQuantizer import BaseQuantizer

'''
Class that defines workflow of 
'''
class BaseWorkflow:
    def __init__(self):
        self.initializeWorkflow()
    
    def initializeWorkflow(self):
        self.config = BaseConfig()
        # self.report = BaseReport()
        print('Base workflow Initialized')
        
    def prepareModal(self, modelPath, labelPath, inputPath):
        self.inference = BaseInference(modelPath, labelPath, inputPath)
        
        self.inference.isQuantizationNecessary()
            # quantizedModelPath = BaseQuantizer(modelPath)
            # self.inference = BaseInference(quantizedModelPath, labelPath, inputPath)

    def run(self):
        modelDirectories = self.config.getValidModelPath()
        
        for directoryName in modelDirectories:
            modelPath = modelDirectories[directoryName]["model"]
            labelPath = modelDirectories[directoryName]["label"]
            inputPath = modelDirectories[directoryName]["input"]
            print("targeting", modelDirectories[directoryName])
            self.prepareModal(modelPath, labelPath, inputPath)
            
            self.inference.run()
            
            
            
            
            
            
             
