from src.base.BaseInference import BaseInference
from tflite_runtime.interpreter import Interpreter
from pycoral.utils.edgetpu import make_interpreter


class CustomInference(BaseInference):
    def isValidmodel(self):
        return not super().isValidmodel()

    def isQuantizationNecessary(self):
        return super().isQuantizationNecessary()

    def initializeInterpreter(self):
        self.interpreter = make_interpreter(self.modelPath, device=':0')

        if self.isValidmodel():
            self.interpreter.allocate_tensors()
            return True
        
        return False

