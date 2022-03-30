import numpy as np
import matplotlib.pyplot as plt
import random
from random import shuffle
import seaborn as sns
import math
from pprint import pprint
import matplotlib
from matplotlib.cm import cool
import csv
import matplotlib.gridspec as gridspec
import matplotlib.colors as colors
import geopandas as gpd
import pandas as pd
import pysal
import libpysal
from libpysal.weights import KNN
from splot.libpysal import plot_spatial_weights
import fiona
import branca
import folium

m = folium.Map(location=[34.8021, 38.9968], zoom_start=7.2) #zoom_start=13
# m = folium.Map(location=[34.8021, 38.9968], zoom_start=7.2, tiles= "https://api.mapbox.com/v4/mapbox.run-bike-hike/{z}/{x}/{y}.png?access_token=sk.eyJ1IjoiemFocmFqYWZhcmkiLCJhIjoiY2t1ZThuNmRoMWVxajJxbXh5MTBsMDhzOCJ9.oX35NvS5itEDhWMgd8ibSQ" )
m
m.save("index.html")

def calc_d_rate():
    govlabels = ["Aleppo","Damascus","Dar'a","Deir-ez-Zor","Hama","Al Hasakeh","Homs","Idleb","Lattakia","Quneitra","Ar-Raqqa","Rural Dam.","As-Sweida","Tartus","Lebanon","Turkey","Iraq", "Jordan"]

    fc = []
    # for fn in ["destination-social-jordan.csv", "destination-social-scenario0.csv" ]:
    # for fn in ["social-tu-jo.csv", "destination-social-scenario0.csv" ]:
    for fn in ["camp_up_trip_9.csv", "social-leb-tu.csv" ]:
    # for fn in ["social-conflict-shift-leb-tu-2.csv", "social-leb-tu.csv" ]:
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
    return difference_in_range

def fancy_map():

    indexes = [6, 1, 11, 13, 2, 3, 4,5, 7, 8, 9, 10, 12, 14 ]
    observable0 = calc_d_rate()
    observable = []
    avgg = []
    for i in range(len(observable0)):
        s = 0.0
        for j in range(len(observable0[0])):
            s+= observable0[i][j]
        avgg.append(s*10.0)
    for i in indexes:
        observable.append(avgg[i-1])
    o =[]
    for i in range(14):
        o.append(observable[i])
    df = pd.DataFrame({'variation': o})
    gdf2 = gpd.read_file("govfile")
    gdf2['variation'] = df

    gdf3 = gpd.read_file("Jordan_shapefile")
    gdf3['variation'] = avgg[17]
    gdf3['NAME_1'] = "Jordan"
    gdf4 = gpd.read_file("Iraq_shapefile")
    gdf4['variation'] = avgg[16]
    gdf4['NAME_1'] = "Iraq"
    gdf5 = gpd.read_file("Turkey_shapefile")
    gdf5['variation'] = avgg[15]
    gdf5['NAME_1'] = "Turkey"
    gdf6 = gpd.read_file("Lebanon_shapefile")
    gdf6['variation'] = avgg[14]
    gdf6['NAME_1'] = "Lebanon"

    a1 = gdf2.append(gdf6)
    a2 = a1.append(gdf5)
    a3 = a2.append(gdf4)
    a4 = a3.append(gdf3)
    divnorm = colors.TwoSlopeNorm(vmin=-0.5, vcenter=0.0, vmax=0.5)
    # colors = ['#8e0152','#c51b7d','#de77ae','#f1b6da','#fde0ef','#e6f5d0','#b8e186','#7fbc41','#4d9221','#276419'] ['#9e0142','#d53e4f','#f46d43','#fdae61','#fee08b','#ffffbf','#e6f598','#abdda4','#66c2a5','#3288bd','#5e4fa2']
    colormap = branca.colormap.StepColormap(
    colors=['#8e0152','#c51b7d','#de77ae','#f1b6da','#fde0ef','#e6f5d0','#b8e186','#7fbc41','#4d9221','#276419'],index=a4['variation'].quantile([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]),vmin=-2.0,vmax=3)
    colormap.caption="Average change of influx from 2nd rearrangement of conflict - Leb-Tu closure"
    # colormap.caption="Average change of influx - Turkey-Jordan closure"
    # colormap.caption="Average discrepancy - Jordan border closure - social influence"
    colormap.position="topleft"
    # colormap = branca.colormap.StepColormap(
    # colors=sns.color_palette("Spectral", 10),index=a4['variation'].quantile([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]),vmin=-1.0,vmax=1.0)
    geoJSON_df = gpd.read_file("all_syr.geojson")


    stategeo = folium.GeoJson(a4,name='Syria', style_function = lambda x: {'fillColor': colormap(x['properties']['variation']), 'color': 'black','weight':1, 'fillOpacity':0.5}, tooltip=folium.GeoJsonTooltip(fields=['NAME_1', 'variation'], aliases=['NAME_1', 'variation'] , localize=True) ).add_to(m)
    colormap.add_to(m)
    folium.LayerControl().add_to(m)
    m.save("index.html")

fancy_map()
