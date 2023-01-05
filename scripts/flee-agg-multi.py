import seaborn as sns
import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt

exp_1=[508,510,586,397,228,274,283,264,474,376,456,327,469,518,726,1271,1135,704,706,706,841,624,594,722,543,620,817,599,386,199,287,235,231,257,219,281,295,397,537,457]
exp_2=[467,497,526,357,227,284,260,299,435,358,564,332,455,471,725,1151,960,664,635,676,751,567,578,635,489,607,724,545,359,211,270,218,228,230,211,263,278,386,468,410]
exp_3=[472,520,536,351,229,297,251,321,441,363,453,343,474,475,783,1203,958,691,640,715,765,574,607,644,499,646,740,553,351,222,277,215,242,233,222,273,287,413,483,424]
exp_4=[0,0,0,0,0,56,361,373,356,399,597,184,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
exp_5=[402,544,569,325,152,182,74,271,391,304,447,247,479,417,978,1604,1081,759,623,833,828,549,716,793,501,804,898,514,143,105,249,96,220,207,213,280,278,534,613,502]

data = [41300.0, 245723.0, 62954.0, 74791.0, 26317.0, 18269.0, 24000.0, 39733.0, 46570.0, 38266.0, 58528.0, 52283.0, 78536.0, 95472.0, 120552.0, 201054.0, 76934.0, 110651.0, 127912.0, 75997.0, 222271.0, 280801.0, 420433.0, 142881.0, 119507.0, 101253.0, 83149.0, 118603.0, 67516.0, 50321.0, 42380.0, 18116.0, 21561.0, 10739.0, 26174.0, 25139.0, 36403.0, 58205.0, 53285.0, 28405.0, 107049.0, 36163.0]

sim = []
with open("flee-exp-03.csv") as f2:
    myf2 = csv.reader(f2,delimiter=',')
    for row in myf2:
        x = []
        for i in range(len(row)-1):
            x.append(float(row[i]))
        sim.append(x)
f2.close()
exp_03 = []
for i in range(len(sim[0])):
    x = 0.0
    for j in range(len(sim)):
        x+=sim[j][i]
    exp_03.append(x)

flee_flow = []
time = []
experiment_no = []

# for j in range(len(exp_1)):
#     experiment_no.append(1)
#     time.append(j)
#     flee_flow.append(exp_1[j])
#     experiment_no.append(2)
#     time.append(j)
#     flee_flow.append(exp_2[j])
#     experiment_no.append(3)
#     time.append(j)
#     flee_flow.append(exp_3[j])
#     experiment_no.append(4)
#     time.append(j)
#     flee_flow.append(exp_4[j])
#     experiment_no.append(5)
#     time.append(j)
#     flee_flow.append(exp_5[j])
for j in range(len(exp_1)):
    experiment_no.append("experiment_1_output")
    time.append(j)
    flee_flow.append(exp_03[j]*2.0)
    experiment_no.append("experiment_2_output")
    time.append(j)
    flee_flow.append(exp_3[j]*2.0)
    experiment_no.append("aggregate_flow_data")
    time.append(j)
    flee_flow.append(data[j]/100.0)

d = {"Flee_flow": experiment_no , "month": time, "flow_count (x 100)": flee_flow}
df_all = pd.DataFrame.from_dict(d)

sns.set_theme(style="darkgrid")
# palette = sns.color_palette("mako_r", 5)
palette = sns.color_palette("rocket_r", 3)
g = sns.lineplot(
    data=df_all, x="month", y="flow_count (x 100)",
    hue="Flee_flow",
    palette= palette
)
l1 = g.lines[0]
l2 = g.lines[1]
l3 = g.lines[2]
x1 = l1.get_xydata()[:,0]
y1 = l1.get_xydata()[:,1]
x2 = l2.get_xydata()[:,0]
y2 = l2.get_xydata()[:,1]
x3 = l3.get_xydata()[:,0]
y3 = l3.get_xydata()[:,1]
g.fill_between(x1,y1, color=palette[0], alpha=0.3)
g.fill_between(x2,y2, color=palette[1], alpha=0.3)
g.fill_between(x3,y3, color=palette[2], alpha=0.3)

figure = g.get_figure()
figure.savefig('flee-agg-3-vs-data.png', dpi=400)
