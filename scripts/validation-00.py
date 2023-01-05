import seaborn as sns
import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt
import math

def SRMSE( sim_arr, data_arr):
    init_sizes = [23000, 11050, 4975, 6000, 7950, 6350, 8800, 7300, 6375, 425, 4575, 14150, 1800, 3925]
    st_errors = []
    # summ_abs = 0.0;
    # summ_sq = 0.0;
    for i in range(len(sim_arr)):
        x = []
        for j in range(len(sim_arr[0])):
            x0 = 0.0
            x0 = abs(sim_arr[i][j] - data_arr[i][j])/(200.0*init_sizes[i])
            # summ_sq += pow(x0,2)
            # summ_abs += x0
            x.append(x0)
        st_errors.append(x)

    # print("MSPE= ")
    # print(1.0*summ_sq/(len(sim_arr)*len(sim_arr[0])))
    # print("MAPE= ")
    # print(1.0*summ_abs/(len(sim_arr)*len(sim_arr[0])))
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

st_errors_v = []
for i in range(len(fc)):
    x = SRMSE(fc[i], idp)
    st_errors_v.append(x)

govlabels = ["Aleppo","Damascus","Dar'a","Deir-ez-Zor","Hama","Al Hasakeh","Homs","Idleb","Lattakia","Quneitra","Ar-Raqqa","Rural Damascus","As-Sweida","Tartus"]

section = []
l_title = []
experiment = []
errors = []
months = []
govs = []
flow_counts = []

# for i in range(len(st_errors_v)):
#     for j in range(len(st_errors_v[i])): #14
#         for k in range(len(st_errors_v[i][j])): #40
#             if(i <4 ):
#                 section.append('validation')
#                 l_title.append('validation '+str(i))
#                 experiment.append(i)
#                 months.append(k)
#                 govs.append(govlabels[j])
#                 errors.append(st_errors_v[i][j][k])
#             else:
#                 section.append('calibration')
#                 l_title.append("calibration")
#                 experiment.append(i)
#                 months.append(k)
#                 govs.append(govlabels[j])
#                 errors.append(st_errors_v[i][j][k])
for i in range(len(fc)):
    for j in range(len(fc[i])): #14
        for k in range(len(fc[i][j])): #40
            if(i <4 ):
                section.append('validation')
                experiment.append(i)
                months.append(k)
                govs.append(govlabels[j])
                flow_counts.append(fc[i][j][k])
            else:
                section.append('calibration')
                experiment.append(i)
                months.append(k)
                govs.append(govlabels[j])
                flow_counts.append(fc[i][j][k])
for j in range(len(idp)):
    for k in range(len(idp[j]) -2):
        section.append("observed_data")
        experiment.append(5)
        months.append(k)
        govs.append(govlabels[j])
        flow_counts.append(idp[j][k])

# d = {"experiment": l_title , "gov": govs, "month": months, "absolute-error": errors}
d = {"experiment-k": experiment , "category": section, "gov": govs, "month": months, "flow-count": flow_counts}
df_all = pd.DataFrame.from_dict(d)
sns.set_theme(style="darkgrid")

# g = sns.relplot(
#     data=df_all,
#     x="month", y="absolute-error", col="gov", hue = "experiment",
#     kind="line", palette="rocket_r", linewidth=2, zorder=4,
#     col_wrap=2, height=1.7, aspect=2.3, legend=True, facet_kws={"sharey":False},
# )


g = sns.relplot(
    data=df_all,
    x="month", y="flow-count", col="gov", hue="category",
    kind="line", palette="rocket_r", linewidth=2, zorder=6,
    col_wrap=2, height=1.7, aspect=2.3, legend=True, facet_kws={"sharey":False},
)
#
# for gov, ax in g.axes_dict.items():
#
#     # Add the title as an annotation within the plot
#     # ax.text(.8, .85, year, transform=ax.transAxes, fontweight="bold")
#
#     # Plot every year's time series in the background
#     a = ( df_all['category'] == "validation" ) & ( df_all['gov'] == gov )
#     sns.lineplot(
#         data=df_all[a], x="month", y="flow-count", units="experiment",
#         estimator=None, color=".7", linewidth=1, ax=ax, legend = False
#     )
#
# g.savefig('validation-error-all.png')

# a = df_all['category'] == "validation"
# palette = sns.color_palette("crest", 4)
# g = sns.relplot(
#     data=df_all[a],
#     x="month", y="flow-count", col="gov", hue = "experiment-k",
#     kind="line", palette="crest", alpha = 0.4, linewidth=2, zorder=4,
#     col_wrap=2, height=1.7, aspect=2.3, legend=True, facet_kws={"sharey":False},
# )

# for gov, ax in g.axes_dict.items():
#
#     # Add the title as an annotation within the plot
#     # ax.text(.8, .85, year, transform=ax.transAxes, fontweight="bold")
#
#     # Plot every year's time series in the background
#     a = (df_all['category'] == "observed_data") & ( df_all['gov'] == gov )
#     b = sns.lineplot(
#         data=df_all[a], x="month", y="flow-count",
#         estimator=None, color = 'black', alpha = 0.4, linewidth=1, ax=ax, legend = False
#     )
    # print(b.lines)
    # l1 = b.lines[4]
    # x1 = l1.get_xydata()[:,0]
    # y1 = l1.get_xydata()[:,1]
    # b.fill_between(x1[0:10],y1[0:10], color=palette[0], alpha=0.3)
    # b.fill_between(x1[10:20],y1[10:20], color=palette[1], alpha=0.3)
    # b.fill_between(x1[20:30],y1[20:30], color=palette[2], alpha=0.3)
    # b.fill_between(x1[30:40],y1[30:40], color=palette[3], alpha=0.3)

g.savefig('flee-errors.png')
