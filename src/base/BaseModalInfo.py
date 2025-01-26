import pycoral.utils.dataset import read_label_file
class BaseModalInfo:
    def __init__(self):
        self.labels = ''
        pass
    
    def initializeModalInfo(self):
        self.labels = self.readLabels('labels.txt')
    
    def getReadLabels(self, file_name):
        self.labels = read_label_file(file_name)
        pass
    
    def getModalSize(self, file_name):
        pass
    
    def getInputDetails(self):
        pass
    
    def getOutputDetails(self):
        pass
        
    
    