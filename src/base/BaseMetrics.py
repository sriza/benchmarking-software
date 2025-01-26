
import time
from pycoral.learn.backprop.softmax_regression import get_accuracy

'''
Class to collect data based on different metrics
'''
class BaseMetrics:
    def __init__(self):
        self.timer = 0
        self.initializeMetrics()  
        
    def initializeMetrics(self):
        print("Base Metrics Initialized")
            
    def startTimer(self):
        self.timer = time.perf_counter()
        pass
    
    def endTimer(self):
        self._resetTimer()
        pass
    
    def temperature(self):
        pass
    
    def power(self):
        pass
    
    def accuracy(self, mat_x,  labels):
        get_accuracy(mat_x, labels)
        pass
    
    def _resetTimer():
        self.timer = 0
        pass
    
    def _storeMetrics():
        pass
        
    
