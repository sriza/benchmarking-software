
# Requirements
Python: 3.9

Pip: 25.0


# Important packages
Though the packages are listed in requirement.txt file, the installation might not completely work. Thus, these are list of important packages used in the project:
- Tensorflow
- Pycoral
- Pillow
- Matplotlib
- Numpy

# Running the project
- Clone the project into your local environment. It is recommended to use virtual environment to ensure that the version of packages and python is correct. At the time of the creation of this project, pycoral doesn't work for python version greater than 3.9.
- Install all the important packages in the virtual environment.
- Set up the config.json file based on example file.
- Run the project with `python main.py` command.

# Understanding config file

```
{
    "device": "coral_tpu",
    "models": ["tflite"],
    "inference_attempts":"10",
    "report_format": "csv",
    "modelTask":{
        "EfficientDet-Lite0":  "detect",
        "EfficientDet-Lite3":  "detect",
        "EfficientNet(L)": "classify",
        "InceptionV1": "classify",
        "InceptionV3": "classify",
        "MobileNetV1": "classify",
        "MobileNetV2": "classify",
        "MobileNetV3": "classify",
        "ResNet-50": "classify",
        "SSDLiteMobileDet":  "detect",
        "SSDMobileNetV1":  "detect",
        "SSDMobileNetV2":  "detect"
    }
}
```

By default base model is used. Create a file named 'config.json' to customize these parameters, please ensure the name of device is similar to the folder name in custom folder.
<b>Device</b> 
<b>Models</b> can contain list of extension different models that device can run.

<b>Inference_attempts</b> is number of inference to be done on model.

<b>Report_format</b> refers to format in which the output file should be. By default csv file is created. This can be later extended to create report in different formats.

<b>Model_task</b> contains the key value pair of different models and the type of task they perform, object detection as detect, object classification as classify.

# Understanding base classes
- <b>BaseConfig</b>: Reads the configuration parameter from JSON files, merges them, and creates
configuration parameters for benchmarking.
- <b>BaseInference</b>: Loads model, feeds input, and collects the benchmarking metrics based on infer-
ence.
- <b>BaseReport</b>: Creates a CSV file, stores benchmarking output, and creates bar graphs to compare
different models based on metrics.
- <b>BaseWorkflow</b>: Structures the steps to access models, run inference, and create a report with the
help of Inference and Report class.


# Customizing Benchmarking Software
- Customization starts with creating the’config.json’file. In this file, configure the parameter `de-
vice`. The value assigned to base should match the name of the folder to be created within the
`custom benchmarking` folder. Make sure the value to models is also relevant to the device.
- If additional models are to be appended to the existing model, please place them within the `models`
folder and enter the type of task each model does within the `modelTask` parameter of the config file.
- Next, create a folder within the ‘custom benchmarking’ folder with a name that matches the value
assigned to `device`.
- The classes within the base folder can now be inherited and customized within this folder. The inherited
classes must use a classname with the prefix `Custom` instead of `Base`.
- Once the custom classes are completed, you can port the software to the desired base hardware and
conduct benchmarking.