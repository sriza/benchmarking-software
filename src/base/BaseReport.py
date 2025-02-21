import csv
import matplotlib
matplotlib.use('Agg')  # Set the backend to 'Agg'
import matplotlib.pyplot as plt
import pandas as pd
import datetime
import os

'''
Class to generate report visualization
'''
class BaseReport:
    def __init__(self, header):
        self.initializeReport(header)
    
    def initializeReport(self, header):
        self.setFilePath()
        self.filepath = self.filepath
        self.createCSVFile(header)
        print('Base Report has been initialized')
        pass

    def setFilePath(self):
        self.folderpath = "./result/"+datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

        if not os.path.exists(self.folderpath):
            os.makedirs(self.folderpath)

        self.filepath=  self.folderpath+"/report.csv"
    
    def createCSVFile(self, header):
        self.file = open(self.filepath,'w', newline="")
        self.writer = csv.DictWriter(self.file, header)
        self.writer.writeheader()
        
    def appendToReport(self, data):
        self.writer.writerow(data)
        print('Report has been saved to csv file')

    def closeFile(self):
        self.file.close()

    def plotBarGraph(self, df,column, xlabel, ylabel, task):
        plt.figure(figsize=(10, 12))
        plt.bar(df['model_name'], df[column])
        plt.title(f'bar plot of {column} for {task}')
        
        # Add values above each bar
        for i, value in enumerate(df[column]):
            plt.text(i, value + 0.02, str(round(value,2)), ha='center', va='bottom')
            
        plt.autoscale(enable=True, axis='y', tight=False)
        plt.margins(y=0.1)
        
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.xticks(rotation=45, ha='center')
        plt.savefig(f'{self.folderpath}/{column}_bar_plot_{task}.png', dpi=300)

    def visualizeReport(self):
        self.closeFile()
        print('------------------visualizing Report--------------')
        df = pd.read_csv(self.filepath)

        task_types = set(df['task'])

        for task_name in task_types:
            task_df = df[df["task"] == task_name]
            self.plotBarGraph(task_df, 'inference_time', 'model', 'Inference Time (ms)', task_name)
            self.plotBarGraph(task_df, 'model_size', 'model', 'Model Size (MB)', task_name)
            self.plotBarGraph(task_df, 'accuracy', 'model', 'Accuracy', task_name)
        
        print('Reports successfully stored at location:',self.folderpath)

    def compareReport(self):
        pass