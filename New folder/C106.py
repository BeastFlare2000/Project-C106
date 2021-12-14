import csv
import plotly.express as px
import numpy as np

def function(datapath):
    a = []
    b = []
    with open(datapath) as f:
        df = csv.DictReader(f)
        for row in df:
            a.append(float(row['Marks In Percentage']))
            b.append(float(row['Days Present']))
    return{'x':'Marks In Percentage','y':'Days Present'}
def function2(datasource):
        corelation = np.corrcoef(datasource['x'],datasource['y'])
        print(corelation[0,1])
def function3():
        datapath = 'mark.csv'
        datasource = function(datapath)
        function2(datasource)