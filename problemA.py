import csv

def pressuresurgecalc():
    nps = input("What is the nominal pipe size?")

    with open("PipeData.csv") as PipeData:
        csv_reader = csv.reader(PipeData)

        for row in csv_reader:
            if nps == row[0]:
                Do = row[1]
    