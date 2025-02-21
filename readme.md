

# Running the project


# Understanding config file

```
{
    "device": "coral_tpu",
    "models": ["tflite"],
    "alternative_models": ["pb"],
    "quantization": {
        "datatype": "int8"
    },
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

models can contain list of extension different models that device can run.

Alternative models is optional parameter can contain extension of models that are convertable to models. Please note, for this case you need to extend base class to convert the alternative extension to required extension.

Quantization is optional parameter that contains the type of quantization that is to be done to given model.

Inference_attempts is number of inference to be done on model.

Report format refers to format in which the output file should be. By default csv file is created. This can be later extended to create report in different formats.

Model task contains the key value pair of different models and the type of task they perform, object detection as detect, object classification as classify.


