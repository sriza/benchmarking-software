import csv
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
        print('Base Report has been initialized')
        self.writer.writerow(data)

    def closeFile(self):
        self.file.close()

    def plotBarGraph(self, df,column, xlabel, ylabel, task):
        plt.figure(figsize=(8, 4))
        plt.bar(df['modal_name'], df[column])
        plt.title(f'bar plot of {column} for {task}')
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.savefig(f'{self.folderpath}/{column}_bar_plot_{task}.png')
        plt.show()

    def visualizeReport(self):
        self.closeFile()
        self.file = open(self.filepath,'w', newline="")
        self.writer = csv.DictReader(self.file)
        print('visualizing Report')
        df = pd.read_csv(self.filepath)

        task_types = set(df['task'])

        for task in task_types:
            self.plotBarGraph(df, 'inference_time', 'modal', 'Inference Time (ms)', task)
            self.plotBarGraph(df, 'modal_size', 'modal', 'Model Size (MB)', task)
            self.plotBarGraph(df, 'accuracy', 'modal', 'Accuracy', task)

    def compareReport(self):
        pass


