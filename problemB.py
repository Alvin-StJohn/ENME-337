import csv
import matplotlib.pyplot as plt
import statistics as st
import numpy as np
import math as m
B = 5
W = 30
avsNfile = open("/Users/camla/OneDrive/Desktop/ENME 337/ENME-337/avsN.csv", "r")
avsNdata = csv.reader(avsNfile, delimiter=",")
header = next(avsNdata)
a = []
N = []

for row in avsNdata:
    if not (row):
        continue
    N.append(float(row[0]))
    a.append(float(row[1]))


    
values = list((map(list,zip(N,a))))


plt.title("Crack depth (a) as a function of no. of cycles (N)")
plt.xlabel("no. of cycles (N)")
plt.ylabel("Crack depth (a)")
plt.plot(N,a)
plt.show()

sec = []
for i in range(0,len(values)):
    if i == len(values) - 1:
        break
    calc = (((values[i+1][0]) - (values[i][0])) / ((values[i+1][1]) - (values[i][1])))
    sec.append(calc)

aav = []
for i in range(0,len(a)):
    if i == len(a) - 1:
        break
    calc = (a[i+1] + a[i])/2
    aav.append(calc)

delk = []
for i in aav:
    calc = (((m.pow(10,-6))*(6.14-0.089)*(m.sqrt(i)))/(B*W))*(30.96-(195.8*(i/W))+(730.6*m.pow(i/W,2))-(1186.3*m.pow(i/W,3))+(754.6*m.pow(i/W,4)))
    delk.append(calc)
plt.figure()
x = np.array(np.log(delk))
y = np.array(np.log(sec))
plt.scatter(x,y)
plt.title("fatigue crack growth rate as a function of delta K")
plt.xlabel("log of delta K")
plt.ylabel("log of da/dN")
m, b = np.polyfit(x,y,1)
plt.plot(x, m*x + b)
plt.show()

A = b
n = m

