import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import csv
from string import ascii_letters


govlabels = ["Aleppo","Damascus","Dar'a","Deir-ez-Zor","Hama","Al Hasakeh","Homs","Idleb","Lattakia","Quneitra","Ar-Raqqa","Rural Dam.","As-Sweida","Tartus","Lebanon","Turkey","Iraq", "Jordan"]

fc = []
for fn in ["destination-social-iraq.csv", "destination-scenario0.csv" ]:
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
        x = fc[0][i][j]/(1.0*sums[j]) - fc[1][i][j]/(1.0*sums[j])
        each_gov.append(x)
    difference_in_range.append(each_gov)

d = pd.DataFrame(data=np.array(difference_in_range).T.tolist(),columns=list(govlabels))


sns.set_theme(style="white")

# Compute the correlation matrix
corr = d.corr(method ='spearman')

# Generate a mask for the upper triangle
mask = np.triu(np.ones_like(corr, dtype=bool))

# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(8, 7))

# Generate a custom diverging colormap
# cmap = sns.diverging_palette(145, 300, s=60, as_cmap=True)
cmap = sns.color_palette("Spectral", as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
g = sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})
plt.savefig('social-ir-closure-corr.png')
plt.show()
