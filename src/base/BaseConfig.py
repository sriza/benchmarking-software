import json
from pathlib import Path
import os.path

'''
Class to define configurations to run workflow
'''
class BaseConfig:
    def __init__(self):
        self._defaultConfigFileName = './default_config.json'
        self._configFileName = './config.json'
        self._benchmarkingParameters = {}
        self.initializeBaseConfig()
        
    def initializeBaseConfig(self):
        print("BaseConfig Initialized")
        # get set and check configurations
        self._getConfiguration()
        self._setConfiguration()
        self._checkValidityOfParameters()
        
        # get relevant modals
        self._collectModalPaths()
        
    
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
        for param in self._defaultConfiguration:
            self.setBenchmarkingParameters(param)
            
        print(self._defaultConfiguration)
        print(self._customConfiguration)
        print(self._benchmarkingParameters)
        
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
    
    def _collectModalPaths(self):
        
        
    
    def getModalPaths(self):
        pass
    
    