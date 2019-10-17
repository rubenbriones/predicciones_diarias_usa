# -*- coding: utf-8 -*-
"""
Created on Wed May 29 16:47:06 2019

@author: Ruben
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statistics import mean, median

path = "tradingsim_2019mayojunio_normalizadoPorVolatilidad.csv"
data = pd.read_csv(path, sep=";")

marcoObjetivo = '1D-15M_c'

#sns.lmplot(x='gap', y=marcoObjetivo, hue='color', data=data, palette=dict(verde="g", rojo="r"))
#sns.lmplot(x='gap', y=marcoObjetivo, hue='color', data=data[data['gap'].isnull()], palette=dict(verde="g", rojo="r"))
#data=data.fillna(0)
#sns.lmplot(x='gap', y=marcoObjetivo, hue='color', data=data, palette=dict(verde="g", rojo="r"))
#sns.lmplot(x='gap', y=marcoObjetivo, hue='color', data=data[data['gap'].isnull()], palette=dict(verde="g", rojo="r"))
#sns.lmplot(x='gap', y=marcoObjetivo, hue='color', data=data[data['gap']==0], palette=dict(verde="g", rojo="r"))
#sns.lmplot(x='gap', y=marcoObjetivo, hue='color', data=data[data['gap']!=0], palette=dict(verde="g", rojo="r"))

sns.lmplot(x='15M_c', y=marcoObjetivo, hue='color', data=data, palette=dict(verde="g", rojo="r"))





