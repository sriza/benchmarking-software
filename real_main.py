
from src.base.BaseConfig import BaseConfig

try:
    
    # read config file
    config = BaseConfig()

    # get the models folder to find number of models and compatible models
    # pass this data to Workflow
        # loop over possible modals
            # get modal info
            # check need of quantization or conversion and convert if needed
            # get inputs and run inference
            # get metrics 
            # add to temporary report file
    # get final report file
    # convert report file to visualizable format
    # end program and delete 
    
except Exception as e:
    print("error occurred", e)
finally:
    print("ending program")