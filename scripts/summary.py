import seaborn as sns
import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt
import math

def calc_d_rate(f_name1, f_name2):
    fc = []
    for fn in [f_name1, f_name2 ]:
    # for fn in ["social-tu-jo.csv", "destination-social-scenario0.csv" ]:
    # for fn in ["social-conflict-shift-leb-jo.csv", "social-conflict-shift.csv" ]:
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

    sums = []
    for j in range(len(fc[1][0])):
        x = 0.0
        for i in range(len(fc[1])):
            x += fc[0][i][j]
        sums.append(x)

    difference_in_range = []
    for i in range(18):
        each_gov = []
        for j in range(9,19):
            x = ( fc[0][i][j] - fc[1][i][j] )/(1.0*sums[j])
            each_gov.append(x)
        difference_in_range.append(each_gov)
    avgg = []
    for i in range(len(difference_in_range)):
        s = 0.0
        for j in range(len(difference_in_range[i])):
            s+= difference_in_range[i][j]
        avgg.append(s*10.0)
    # return difference_in_range
    return avgg

def crt_df():
    file_names = [ "destinationalllebclosed.csv", "destination-social-alllebclosed.csv", "destinationallturkeyclosed.csv", "destination-social-turkey.csv", "destination-iraq.csv", "destination-social-iraq.csv", "destination-jordan.csv", "destination-social-jordan.csv"]
    govlabels = ["Aleppo","Damascus","Dar'a","Deir-ez-Zor","Hama","Al Hasakeh","Homs","Idleb","Lattakia","Quneitra","Ar-Raqqa","Rural Damascus","As-Sweida","Tartus","Lebanon","Turkey","Iraq", "Jordan"]
    experiment_labels = [ "Destination choice model", "Lebanese border closure", "Turkish border closure", "Iraqi border closure", "Jordan border closure", "Social influence model", "Lebanon closure-social influence", "Turkey closure-social influence", "Iraq closure-social influence", "Jordan closure-social influence" ]
    experiment = []
    errors = []
    govs = []

    all_diffs=[]
    for i in range(len(file_names)):
        if(i%2 != 0):
            all_diffs.append(calc_d_rate(file_names[i],"destination-social-scenario0.csv"))
        else:
            all_diffs.append(calc_d_rate(file_names[i],"destination-scenario0.csv"))

    # for i in range(len(all_diffs)):
    #     for j in range(len(all_diffs[i])):
    #         experiment.append(experiment_labels[i+1])
    #         govs.append(govlabels[j])
    #         errors.append(all_diffs[i][j])
    d = {"Lebanon closure-social influence": all_diffs[0], "Turkey closure-social influence": all_diffs[1] , "Iraq closure-social influence": all_diffs[2] , "Jordan closure-social influence": all_diffs[3], "Lebanon-Jordan border closure": all_diffs[4], "Lebanon-Turkey closure": all_diffs[5], "Lebanon-Iraq closure": all_diffs[6], "Turkey-Jordan closure": all_diffs[7], "gov": govlabels}
    df_all = pd.DataFrame.from_dict(d)
    return df_all

def dot_plot():
    sns.set_theme(style="darkgrid")
    df = crt_df()
    g = sns.PairGrid(df,x_vars=df.columns[:-1], y_vars=["gov"],height=10, aspect=.21)
    g.map(sns.stripplot, size=7, orient="h", jitter=False,palette="viridis", linewidth=1, edgecolor="w")
    g.set(xlabel="Average change of inflow", ylabel="")
    titles = ["Lebanon closure", "Lebanon closure-social influence", "Turkey closure", "Turkey closure-social influence", "Iraq closure", "Iraq closure-social influence", "Jordan closure", "Jordan closure-social influence" ]
    # g.set(xlim=(-10,10))
    sns.set(font_scale=0.9)
    i = 0
    for ax, title in zip(g.axes.flat, titles):

        # Set a different title for each axes
        ax.set(title=title)

        # Make the grid horizontal instead of vertical
        ax.xaxis.grid(True)
        ax.yaxis.grid(True)

    sns.despine(left=True, bottom=True)
    plt.show()
    g.savefig("summary_dot_2_n.png")

dot_plot()
