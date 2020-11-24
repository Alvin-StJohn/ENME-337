import csv
import pandas as pd

def pressuresurgenumb():
    nps = input("What is the nominal pipe size?")

    data = pd.read_csv("PipeData.csv", header=None, delimiter=r"\s+")

    for row in data:
        if row[0] == nps:
            Do = row[1]
            pipsched = row[2]
            t = row[3]
            
            if type(pipsched) != type(1):
                pipsched = float(input("A pipe schedule number was not valid, please input a pipe schedule number."))
        
        else:
            print("The nominal pipe size was not found.")

    data1 = pd.read_csv("MaterialData.csv", header=None, delimiter=r"\s+")

    