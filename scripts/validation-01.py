import seaborn as sns
import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt
import math

def SRMSE( sim_arr, data_arr):
    init_sizes = [23000, 11050, 4975, 6000, 7950, 6350, 8800, 7300, 6375, 425, 4575, 14150, 1800, 3925]
    st_errors = []
    summ_abs = 0.0;
    summ_sq = 0.0;
    for i in range(len(sim_arr)):
        x = []
        for j in range(len(sim_arr[0])):
            x0 = 0.0
            x0 = abs(sim_arr[i][j] - data_arr[i][j])/(200.0*init_sizes[i])
            summ_sq += pow(x0,2)
            summ_abs += x0
            x.append(x0)
        st_errors.append(x)

    print("MSPE= ")
    print(1.0*summ_sq/(len(sim_arr)*len(sim_arr[0])))
    print("MAPE= ")
    print(1.0*summ_abs/(len(sim_arr)*len(sim_arr[0])))
    return st_errors


refugees = [ 2170.0,188572.0,28955.0,36515.0,9227.0,4350.0,2216.0,728.0,6675.0,21266.0,11700.0,50368.0,41436.0,56760.0,60218.0,25967.0,1194.0,58860.0,57382.0,792.0,101199.0,44580.0,108482.0,65269.0,58312.0,65556.0,37149.0,24981.0,9656.0,505.0,1836.0,85.0,18857.0,23104.0,19351.0,15115.0,18789.0,4235.0,7522.0,0.0,130.0,11308.0 ]
idp = []
with open("nlf.csv") as f1:
    myf1 = csv.reader(f1,delimiter = ',')
    for row in myf1:
        x = []
        for i in range(len(row)-1):
            x.append(float(row[i]))
        idp.append(x)

fpermonth = []
for i in range(len(idp[0])):
    x = 0.0
    for j in range(len(idp)):
        x+= idp[j][i]
    fpermonth.append(x)

for i in range(len(idp)):
    for j in range(len(idp[0])):
        idp[i][j] += refugees[j]*1.0*idp[i][j]/(1.0*fpermonth[j])

fc = []
for fn in ["simres-f-cv-00.csv", "simres-f-cv-01.csv", "simres-f-cv-02.csv", "simres-f-cv-03.csv", "flee-exp-03.csv"]:
    sim = []
    with open(fn) as f2:
        myf2 = csv.reader(f2,delimiter=',')
        for row in myf2:
            x = []
            for i in range(len(row)-1):
                x.append(200.0*float(row[i]))
            sim.append(x)
    f2.close()
    fc.append(sim)

SRMSE(fc[3], fc[4] )
