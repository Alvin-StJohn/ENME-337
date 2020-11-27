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
    header = next(Ygraphdata)

    c = b/2
    line = a/c
    x = a/values[2]

    if line >= 0.9:
        x = x
        line1 = 1.0
        x1 = 10
        y2 = 11
    elif line < 0.9 and line >= 0.6:
        x = x**4
        line1 = 0.8
        x1 = 8
        y2 = 9
    elif line < 0.6 and line > 0.3:
        x = x**3
        line1 = 0.4
        x1 = 6
        y2 = 7
    elif line <= 0.3 and line > 0.15:
        x = x**4
        line1 = 0.2
        x1 = 4
        y2 = 5
    elif line <= 0.15 and line > 0.14:
        x=x**4
        line1 = 0.1
        x1 = 2
        y1 = 3
    else:
        x=x**4
        line1 = 0.02
        x1 = 0
        y1 = 1

    xvalues = []
    yvalues = []
    for rows in Ygraphdata:
        xvalues.append(rows[x1])
        yvalues.append(rows[y1])
    
    for i in range(xvalues):
        if xvalues[i] == x:
            Y = yvalues[i]

    '''
    if wall == 'thin-wall':
    
    else:
    '''




    


