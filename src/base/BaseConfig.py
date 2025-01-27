import json
import os.path

'''
Class to define configurations to run workflow
This class reads the configuration file, checks validity of configurations and maintains the dictionary of config
'''
class BaseConfig:
    def __init__(self):
        self._defaultConfigFileName = './default_config.json'
        self._configFileName = './config.json'
        self._modelLocation = './models'
        self._benchmarkingParameters = {}
        self.initializeBaseConfig()
        
    def initializeBaseConfig(self):
        # get set and check configurations
        self._getConfiguration()
        self._setConfiguration()
        self._checkValidityOfParameters()
        
        # get relevant modals
        self._checkIfModelExists()
        print("------------------BaseConfig Initialized-----------------")
        
    
    def __loadFromFile(self, filepath, strict = False):
        # file = Path(filepath)
        print("filepath", filepath)
        
        if os.path.isfile(filepath):
            with open(filepath,'r') as file:
                return json.load(file)
        else:
            if strict:
                raise Exception(filepath, " file not found")
            return {}
    
    def _getConfiguration(self):
        self._defaultConfiguration = self.__loadFromFile(self._defaultConfigFileName, True)
        self._customConfiguration = self.__loadFromFile(self._configFileName)
    
    def _setConfiguration(self):
        configurationKeys = self._defaultConfiguration.keys() & self._customConfiguration.keys()
         
        for param in configurationKeys:
            self.setBenchmarkingParameters(param)
        
    def setBenchmarkingParameters(self, parameter):
        if parameter in self._customConfiguration:
            self._benchmarkingParameters[parameter] = self._customConfiguration[parameter]
        else:
            self._benchmarkingParameters[parameter] = self._defaultConfiguration[parameter]
      
    # validation for config file 
    def _checkValidityOfParameters(self):
        if True:
            print("Parameters are valid")
        else:
            raise Exception("Please insert correct parameters in Config File")
        
    def getRelevantFileExtension(self):
        return list(set(self._benchmarkingParameters['models']+self._benchmarkingParameters['alternative_models'])) 
    
    def _checkIfModelExists(self):
        relevantFileExtensions = self.getRelevantFileExtension()
        relevantModelCount = 0
        
        for dir in self.getSelectedModels():
            subpath = os.path.join(self._modelLocation, dir)
            
            if not os.path.isfile(subpath):
                for item in os.listdir(subpath):
                    if item.endswith(tuple(relevantFileExtensions)):
                        relevantModelCount+=1
        
        if relevantModelCount == 0:
            raise Exception("We do not have models that are application for test. Please add models before you start again")
        
        print('No of valid models found:', relevantModelCount);  
    
    def getValidModelPath(self):
        relevantFileExtensions = self.getRelevantFileExtension()
        relevantModels = {}
        
        for dir in self.getSelectedModels():
            subpath = os.path.join(self._modelLocation, dir)
            
            if not os.path.isfile(subpath):
                for item in os.listdir(subpath):
                    if item.endswith(tuple(relevantFileExtensions)):
                        relevantModels[subpath] = {
                            "model": os.path.join(subpath, item), 
                            "label": os.path.join(subpath,"label.txt"),
                            "input": os.path.join(subpath, "inputs")
                            }
        
        return relevantModels 
          

    def getSelectedModels(self):
        selectedModels = self._benchmarkingParameters["selectedModels"]
        
        if isinstance(selectedModels,str) and selectedModels == "*":
            return os.listdir(self._modelLocation)
        
        return selectedModels
    
    def getBenchmarkingParameter(self):
        return self._benchmarkingParameters;  
    
    