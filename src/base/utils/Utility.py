import importlib
import os.path

defaultBaseClass = "src.base"
defaultPrefix = "Base"

def getClass(baseClass, prefix, className):
    baseClass = baseClass
    prefix = prefix
    moduleName = f'{baseClass}.{prefix}{className}'
    filePath = moduleName.replace('.','/')+".py"

    if fileExists(filePath):
        module = importlib.import_module(moduleName)
        return getattr(module,f'{prefix}{className}')
    else:
        moduleName = f'{defaultBaseClass}.{defaultPrefix}{className}'
        module = importlib.import_module(moduleName)
        return getattr(module, f'{defaultPrefix}{className}')


def fileExists(filePath):
    if os.path.exists(filePath):
        return True
    
    return False