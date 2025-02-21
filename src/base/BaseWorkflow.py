
from src.base.utils.Utility import getClass

'''
Class that defines workflow of benchmarking
'''
class BaseWorkflow:
    def __init__(self, config, baseClass, prefix):
        self.initializeWorkflow(config, baseClass, prefix)

    
    def initializeWorkflow(self, config, baseClass, prefix):
        self.config = config
        self.baseClass = baseClass
        self.prefix = prefix
        header = ['model_name', 'model_size', 'inference_time', 'accuracy','task']
        ReportClass = getClass(self.baseClass, self.prefix, 'Report')
        self.report = ReportClass(header)
        
    def prepareModel(self, modelPath, labelPath, inputPath):
        InferenceClass = getClass(self.baseClass, self.prefix, 'Inference')
        self.inference = InferenceClass(modelPath, labelPath, inputPath)
        
        if not self.inference.initializeInterpreter():
            print("Invalid model for device")
            return False

        self.inference.initializeModelInfo()
        return True
    
    def benchmark(self):
        modelDirectories = self.config.getValidModelPath()
        inferenceAttempts = int(self.config.getBenchmarkingParameter("inference_attempts"))

        for directoryName in modelDirectories:
            modelName = modelDirectories[directoryName]["name"]
            modelPath = modelDirectories[directoryName]["model"]
            labelPath = modelDirectories[directoryName]["label"]
            inputPath = modelDirectories[directoryName]["input"]

            task = self.config.getBenchmarkingParameter("modelTask")[modelName]
            print(f'-----Preparing Model {modelName} : {task} -----------')
            isPrepared = self.prepareModel(modelPath, labelPath, inputPath)
            modelSize = self.inference.getModelSize()

            if not isPrepared:
                print("skipped model "+ modelName)
                continue

            result = {}
            result["model_name"] = modelName
            result["model_size"] = modelSize
            result["task"] = task
            result["accuracy"] = []
            result["inference_time"] = []

            for i in range(inferenceAttempts):
                tempResult = self.inference.run(task)
                result["accuracy"].append(tempResult["accuracy"])
                result["inference_time"].append(tempResult["inference_time"])

            # result["accuracy"] = sum(result["accuracy"])/inferenceAttempts
            #result["inference_time"] = sum(result["inference_time"])/inferenceAttempts
            result["accuracy"] = result["accuracy"][-1]
            result["inference_time"] = result["inference_time"][-1]
            print('model size:',result['model_size'],'MB\naccuracy:',result["accuracy"], '%\ninference_time',result["inference_time"],'ms')
            self.report.appendToReport(result)

    def run(self):
        self.benchmark()
        self.report.visualizeReport()
        
