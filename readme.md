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
    "metrics" : {
        "temperature":"20",
        "power" :"2",
        "accuracy" :"80",
        "latency": "2"
    },
    "report_format": "csv"
}
```

By default base model is used. Create a file named 'config.json' to customize these parameters, please ensure the name of device is similar to the folder name in custom folder.

Models can contain list of extension different models that device can run.

Alternative models is optional parameter can contain extension of models that are convertable to models. Please note, for this case you need to extend base class to convert the alternative extension to required extension.

Quantization is optional parameter that contains the type of quantization that is to be done to given model.

Inference_attempts is number of inference to be done on modal.

Metrics are json pair of type of metrics and threshold which is acceptable.
- Temperature in degree C
- Power in W
- Accuracy in percentage
- latency in ms

Report format refers to format in which the output file should be. By default csv file is created. There is also option for html file.

## ToDos:
- Add validation for config file
