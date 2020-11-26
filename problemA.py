import csv
import statistics as st

def part1numbers():
    nps = input("What is the nominal pipe size?: ")
    pipsched = input("What is the pipe schedule?: ")
    pipmat = input("What is the pipe material?: ")
    pipefile = open("PipeData.csv", "r")
    pipedata = csv.reader(pipefile)
    rows = list(pipedata)
    
    count=0
    for i in rows:
        t = 0
        if i[count][0] == nps and i[count][2] == pipsched:
            Do = i[count][1]
            t = i[count][3]
        
        elif i[count][0] == nps and i[count][2] != pipsched:
            Do = i[count][1]

        count+=1


    matfile = open("MaterialData.csv", "r")
    matdata = csv.reader(matfile)
    rows2 = list(matdata)
    
    count1=0
    for i in rows2:
        if i[count][0] == pipmat and t != 0:
            Kic = [count][1]
            A = [count][4]
            n = [count][5]
        
        elif i[count][0] == pipmat and t == 0 and i[count][2] != '-':
            t = st.mean([i[count][2],i[count][3]])
        
        elif i[count][0] == pipmat and t == 0 and i[count][2] == '-':
            t = input("Wall thickness could not be calculated please input a number: ")
        count1+=1

    return list(nps,Do,t,Kic,A,n)

values = part1numbers()


def part2numbers(values):
    a = input("What is the initial crack depth?: ")
    b = input("What is the crack length?: ")
    P = input("What is the internal pressure?: ")
    Lf = input("What is the desired lifetime?: ")
    da = input("What is the incremental crack growth?: ")

    if values[1] / values[2] > 20:
        wall = "thin-wall"
    else:
        wall = "thick-wall"

    Ygraphfile = open("YGraphData.csv", "r")
    Ygraphdata = csv.reader(Ygraphfile)
    rows = list(Ygraphdata)

    c = b/2
    line = a/c
    x = a/values[2]

    if abs(line - 1) <= 0.1 or line > 1:
        x = x
    elif line < 0.9 and line >= 0.6:
        x = x**4
    elif line < 0.6 and line > 0.3:
        x = x**3
    else:
        x = x**4

    


