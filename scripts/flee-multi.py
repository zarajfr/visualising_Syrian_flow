import seaborn as sns
import pandas as pd
import csv
import numpy as np

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
for fn in ["flee-exp-1.csv", "flee-exp-2.csv", "flee-exp-03.csv", "flee-exp-4.csv", "flee-exp-5.csv"]:
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

govlabels = ["Aleppo","Damascus","Dar'a","Deir-ez-Zor","Hama","Al Hasakeh","Homs","Idleb","Lattakia","Quneitra","Ar-Raqqa","Rural Damascus","As-Sweida","Tartus"]

exns = []
govs = []
months = []
fcs = []

# for i in range(len(fc)):
#     for j in range(len(fc[i])): #14
#         for k in range(len(fc[i][j])): #40
#             exns.append(i)
#             months.append(k)
#             govs.append(govlabels[j])
#             fcs.append(fc[i][j][k])

for j in range(len(fc[2])): #14
    for k in range(len(fc[2][j])): #40
        exns.append("simulation")
        months.append(k)
        govs.append(govlabels[j])
        fcs.append(fc[2][j][k])

for j in range(len(idp)):
    for k in range(len(idp[j]) -2):
        exns.append("observed_data")
        months.append(k)
        govs.append(govlabels[j])
        fcs.append(idp[j][k])

d = {"Flee_flows": exns , "gov": govs, "month": months, "flow_count": fcs}
df_all = pd.DataFrame.from_dict(d)

# d_data = {""}
# df_all.update({"experiment_no": "Data" , "gov": govs[0], "month": months[0], "flow_count": fcs})

sns.set_theme(style="darkgrid")

g = sns.relplot(
    data=df_all,
    x="month", y="flow_count", col="gov", hue="Flee_flows",
    kind="line", palette="rocket_r", linewidth=2, zorder=6,
    col_wrap=2, height=1.7, aspect=2.3, legend=True, facet_kws={"sharey":False},
)

# #Iterate over each subplot to customize further
# for gov, ax in g.axes_dict.items():
#
#     # Add the title as an annotation within the plot
#     # ax.text(.8, .85, gov, transform=ax.transAxes, fontweight="bold")
#
#     # Plot every year's time series in the background
#     sns.lineplot(
#         data=df_all, x="month", y="flow_count", units="gov",
#         estimator=None, color=".7", linewidth=1, ax=ax,
#     )

g.savefig('1.png')
