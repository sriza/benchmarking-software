
from src.base.BaseConfig import BaseConfig
from src.base.utils.Utility import getClass
import traceback

try:
    defaultBaseClass = "src.base"
    baseClass = defaultBaseClass
    defaultPrefix = "Base"
    prefix = defaultPrefix

    # read config file
    # get the models folder to find number of models and compatible models
    config = BaseConfig()
    device = config.getBenchmarkingParameter("device")
    print(f'Benchmarking for device {device}')

    if not device == "default" :
        baseClass = "src.custom_benchmarking."+device
        prefix = "Custom"

    # pass this data to Workflow
    WorkflowClass = getClass(baseClass, prefix, "Workflow")
    workflow = WorkflowClass(config, baseClass, prefix)
    workflow.run()
    
except Exception as e:
    print("Exception occurred: ", e, traceback.format_exc())
finally:
    print("Benchmarking Completed Successfully")
