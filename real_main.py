
from src.base.BaseWorkflow import BaseWorkflow

try:
    
    # read config file
    # get the models folder to find number of models and compatible models
    # config = BaseConfig().getBenchmarkingParameter()
    
    # pass this data to Workflow
    workflow = BaseWorkflow()
    workflow.run()
        # loop over possible modals
            # get modal info
            # check need of quantization or conversion and convert if needed
            # get inputs and run inference
            # get metrics 
            # add to temporary report file
    # get final report file
    # report = BaseReport()
    # convert report file to visualizable format
    # end program and delete 
    
except Exception as e:
    print("error occurred", e)
finally:
    print("ending program")