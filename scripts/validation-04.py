import seaborn as sns
import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt
import math

def SRMSE( sim_arr, data_arr):
    st_errors = []
    summ_abs = 0.0;
    summ_sq = 0.0;
    for i in range(len(sim_arr)):
        x = []
        for j in range(len(sim_arr[0])):
            x0 = 0.0
            x0 = abs(sim_arr[i][j] - data_arr[i][j])/3863073.0
            summ_sq += pow(x0,2)
            summ_abs += x0
            x.append(x0)
        st_errors.append(x)

    # print("MSPE= ")
    # print(1.0*summ_sq/(len(sim_arr)*len(sim_arr[0])))
    print("MAPE= ")
    print(1.0*summ_abs/(len(sim_arr)*len(sim_arr[0])))
    return st_errors

govlabels = ["Aleppo","Damascus","Dar'a","Deir-ez-Zor","Hama","Al Hasakeh","Homs","Idleb","Lattakia","Quneitra","Ar-Raqqa","Rural Damascus","As-Sweida","Tartus","Lebanon","Turkey","Iraq", "Jordan"]

datadflow = []
with open("finaldestinationflow.csv") as f:
    myf = csv.reader(f, delimiter = ',')
    for row in myf:
        x = []
        for i in range(len(row)-1):
            x.append(float(row[i]))
        datadflow.append(x)
    f.close()

fc = []
# for fn in ["dest-exp-1.csv", "dest-exp-2.csv", "dest-exp-3.csv", "dest-exp-4.csv", "dest-exp-5.csv"]:
#for fn in ["social-ex-1.csv", "social-ex-2.csv", "social-ex-3.csv", "social-ex-4.csv", "social-ex-5.csv"]:
# for fn in ["destination-cv-sp-00.csv", "destination-cv-sp-01.csv", "destination-cv-sp-02.csv", "destination-cv-sp-03.csv", "dest-exp-3.csv" ]:
for fn in ["destination-social-cv-00.csv", "destination-social-cv-01.csv", "destination-social-cv-02.csv", "destination-social-cv-03.csv", "destination-social-cv-sp-00.csv", "destination-social-cv-sp-01.csv", "destination-social-cv-sp-02.csv", "destination-social-cv-sp-03.csv", "dest-exp-3.csv" ]:
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

exns = []
govs = []
months = []
fcs = []

for i in range(len(fc)):
    for j in range(len(fc[i])): #14
        for k in range(len(fc[i][j])): #40
            if(i<8):
                exns.append("validation")
                months.append(k)
                govs.append(govlabels[j])
                fcs.append(fc[i][j][k])
            else:
                exns.append("calibration")
                months.append(k)
                govs.append(govlabels[j])
                fcs.append(fc[i][j][k])

for j in range(len(fc[0])): #14
    for k in range(len(fc[0][j])): #40
        exns.append("data")
        months.append(k)
        govs.append(govlabels[j])
        fcs.append(datadflow[j][k])

for i in range(len(fc)):
    x = SRMSE(fc[i], fc[8])

d = {"experiment_no": exns , "destination": govs, "month": months, "flow_count": fcs}
df_all = pd.DataFrame.from_dict(d)

sns.set_theme(style="darkgrid")

g = sns.relplot(
    data=df_all,
    x="month", y="flow_count", col="destination", hue="experiment_no",
    kind="line", palette="icefire", linewidth=2, zorder=5,
    col_wrap=3, height=1.7, aspect=2.3, legend=True, facet_kws={"sharey":False},
)

# g.savefig('social-destination-all.png')
