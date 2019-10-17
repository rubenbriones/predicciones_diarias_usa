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


data['60m-15m'] = data['60M_c']-data['15M_c']
data['mediodia-15m'] = data['mediodia']-data['15M_c']
data['1dia-15m'] = data['1D_c']-data['15M_c'] #esta col sera muy parecida a la de 1D-15M_c

sns.lmplot(x='15M_c', y='60m-15m', hue='color', data=data, palette=dict(verde="g", rojo="r"))
sns.lmplot(x='15M_c', y='mediodia-15m', hue='color', data=data, palette=dict(verde="g", rojo="r"))
sns.lmplot(x='15M_c', y='1dia-15m', hue='color', data=data, palette=dict(verde="g", rojo="r"))


data['mediodia-60m'] = data['mediodia']-data['60M_c']
data['1dia-60m'] = data['1D_c']-data['60M_c']

sns.lmplot(x='60M_c', y='mediodia-60m', hue='color', data=data, palette=dict(verde="g", rojo="r"))
sns.lmplot(x='60M_c', y='1dia-60m', hue='color', data=data, palette=dict(verde="g", rojo="r"))

