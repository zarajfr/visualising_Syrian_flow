import seaborn as sns
import pandas as pd
import csv
import numpy as np

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
# for fn in ["dest-exp-1.csv", "dest-exp-2.csv", "dest-exp-03.csv", "dest-exp-4.csv", "dest-exp-5.csv"]:
for fn in [ "social-ex-2.csv", "social-ex-3.csv", "social-ex-1.csv", "social-ex-4.csv", "social-ex-5.csv"]:
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
            exns.append(i)
            months.append(k)
            govs.append(govlabels[j])
            fcs.append(fc[i][j][k])


d = {"experiment_no": exns , "destination": govs, "month": months, "flow_count": fcs}
df_all = pd.DataFrame.from_dict(d)

fcs1 = []
exns1 = []
months1 = []
govs1 = []

for j in range(len(fc[2])): #14
    for k in range(len(fc[2][j])): #40
        exns1.append("simulation")
        months1.append(k)
        govs1.append(govlabels[j])
        fcs1.append(fc[2][j][k])


for j in range(len(datadflow)):
    for k in range(len(datadflow[j]) -2):
        exns1.append("observed_data")
        months1.append(k)
        govs1.append(govlabels[j])
        fcs1.append(datadflow[j][k])
d1 = {"Flow": exns1 , "destination": govs1, "month": months1, "flow_count": fcs1}
df_data = pd.DataFrame.from_dict(d1)
# print(df_data)

sns.set_theme(style="darkgrid")

# palette = sns.color_palette("rocket_r", 18)
colors = []
for i in range(18):
    colors.append("#fc5a50")
palette = sns.color_palette(colors)
g = sns.relplot(
    data=df_data,
    x="month", y="flow_count", col="destination", hue="Flow",
    kind="line", palette="rocket_r", linewidth=2, zorder=6,
    col_wrap=3, height=1.7, aspect=2.3, legend=True, facet_kws={"sharey":False},
)

# a = df_all[ 'destination'] == "Aleppo"
# print(a)
# print(df_all[a])
# for destination, ax in g.axes_dict.items():
#
#     # Add the title as an annotation within the plot
#     # ax.text(.8, .85, destination, transform=ax.transAxes, fontweight="bold")
#     # Plot every year's time series in the background
#     a = df_all['destination'] == destination
#     sns.lineplot(
#         data=df_all[a], x="month", y="flow_count", units="experiment_no",
#         estimator=None, color="#5e819d", alpha = 0.5, linewidth=1, ax=ax,
#     )


g.savefig('social-vs-data.png')
# g.savefig('destination-vs-data-err-band.png')
