import seaborn as sns
import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt

def SRMSE( sim_arr, data_arr):
    st_errors = []
    summ_abs = 0.0;
    summ_sq = 0.0;
    for i in range(len(sim_arr)):
        x0 = abs(200.0*sim_arr[i] - data_arr[i])/(200.0*106675.0)
        st_errors.append(x0)
        summ_sq += pow(x0,2)
        summ_abs += x0

    print("MSPE= ")
    print(1.0*summ_sq/(1.0*len(sim_arr)))
    print("MAPE= ")
    print(1.0*summ_abs/(1.0*len(sim_arr)))
    return st_errors

exp_1=[511,536,584,390,228,290,274,296,475,380,609,343,487,515,784,1297,1102,725,701,734,837,620,617,715,540,651,807,588,374,206,286,227,235,247,221,279,291,413,527,453]
exp_2=[440,644,505,261,233,375,160,679,413,620,304,411,569,471,1126,1358,707,791,602,890,717,526,767,596,484,858,703,522,271,287,303,210,299,207,278,304,315,550,476,442]
exp_3=[0,0,31,146,0,0,220,268,498,428,1046,122,0,0,0,288,173,0,49,0,0,94,48,0,0,0,29,0,0,0,27,0,0,0,0,0,0,0,0,0]
exp_4=[482,482,564,378,245,246,236,252,448,349,302,307,460,496,744,1299,1108,694,675,728,850,617,607,727,541,661,839,606,361,228,308,252,279,292,259,324,344,466,586,510]
exp_5=[472,520,536,351,229,297,251,321,441,363,453,343,474,475,783,1203,958,691,640,715,765,574,607,644,499,646,740,553,351,222,277,215,242,233,222,273,287,413,483,424]

data = [41300.0, 245723.0, 62954.0, 74791.0, 26317.0, 18269.0, 24000.0, 39733.0, 46570.0, 38266.0, 58528.0, 52283.0, 78536.0, 95472.0, 120552.0, 201054.0, 76934.0, 110651.0, 127912.0, 75997.0, 222271.0, 280801.0, 420433.0, 142881.0, 119507.0, 101253.0, 83149.0, 118603.0, 67516.0, 50321.0, 42380.0, 18116.0, 21561.0, 10739.0, 26174.0, 25139.0, 36403.0, 58205.0, 53285.0, 28405.0, 107049.0, 36163.0]


errors = []
time = []
experiment_no = []

st_errors_v = []
x = SRMSE(exp_1, data)
st_errors_v.append(x)
x = SRMSE(exp_2, data)
st_errors_v.append(x)
x = SRMSE(exp_3, data)
st_errors_v.append(x)
x = SRMSE(exp_4, data)
st_errors_v.append(x)
x = SRMSE(exp_5, data)
st_errors_v.append(x)

for i in range(len(st_errors_v)):
    for j in range(len(st_errors_v[0])):
        if(i<4):
            experiment_no.append('validation '+str(i+1))
            time.append(j)
            errors.append(st_errors_v[i][j])
        else:
            experiment_no.append('calibration')
            time.append(j)
            errors.append(st_errors_v[i][j])

d = {"experiment": experiment_no , "month": time, "absolute difference": errors}
df_all = pd.DataFrame.from_dict(d)
sns.set_theme(style="darkgrid")
palette = sns.color_palette("rocket_r", 5)
g = sns.lineplot(
    data=df_all, x="month", y="absolute difference",
    hue="experiment",
    palette= palette
)
figure = g.get_figure()
figure.savefig('flee-agg-cv-errors.png', dpi=400)

# flee_flow = []
# time = []
# experiment_no = []
# experiment_type = []
#
# for j in range(len(exp_1)):
#     experiment_no.append("validation-1")
#     time.append(j)
#     flee_flow.append(2.0*exp_1[j])
#     experiment_type.append("validation")
#     experiment_no.append("validation-2")
#     time.append(j)
#     flee_flow.append(2.0*exp_2[j])
#     experiment_type.append("validation")
#     experiment_no.append("validation-3")
#     time.append(j)
#     flee_flow.append(2.0*exp_3[j])
#     experiment_type.append("validation")
#     experiment_no.append("validation-4")
#     time.append(j)
#     flee_flow.append(2.0*exp_4[j])
#     experiment_type.append("validation")
#     experiment_no.append("calibration")
#     time.append(j)
#     flee_flow.append(2.0*exp_5[j])
#     experiment_type.append("calibration")
#     experiment_no.append("aggregate_flow_data")
#     time.append(j)
#     flee_flow.append(data[j]/100.0)
#     experiment_type.append("data")
#
# d = {"Flee_flow": experiment_no , "month": time, "flow_count(x100)": flee_flow, "category": experiment_type} #style = "Flee_flow", markers=False,
# df_all = pd.DataFrame.from_dict(d)
# sns.set_theme(style="darkgrid")
# palette = sns.color_palette("icefire", 3)
# g = sns.lineplot(
#     data=df_all, x="month", y="flow_count(x100)",
#     hue="category",
#     palette= palette
# )
# figure = g.get_figure()
# figure.savefig('flee-agg-cv-all.png', dpi=400)
