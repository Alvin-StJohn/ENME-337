import csv
import pandas as pd

def pressuresurgenumb():
    nps = input("What is the nominal pipe size?")
    pipsched = input("What is the pipe schedule?")
    pipmat = input("What is the pipe material?")
    data = pd.read_csv("PipeData.csv", header=None, delimiter=r"\s+")

    for row in data:
        if row[0] == nps and row[2] == pipsched:
            Do1 = row[1]
            t1 = row[3]
            
            if type(pipsched) != type(1):
                pipsched = float(input("A pipe schedule number was not valid, please input a pipe schedule number."))
        
        else:
            print("The nominal pipe size was not found.")

    data1 = pd.read_csv("MaterialData.csv", header=None, delimiter=r"\s+")

    