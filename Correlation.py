import numpy as np
import csv

def getDataSrc(dataPath):
  present = []
  marks = []
  with open(dataPath) as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
      marks.append(float(row["Marks In Percentage"]))
      present.append(float(row["Days Present"]))

  return{"x": present , "y" : marks}

def findCorrelation(dataSrc):
  correlation = np.corrcoef(dataSrc['x'],dataSrc['y'])
  print(correlation[0,1])

def setup():
  dataPath = "data.csv"
  dataSrc = getDataSrc(dataPath)
  findCorrelation(dataSrc)

setup()