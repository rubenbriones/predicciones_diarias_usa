# -*- coding: utf-8 -*-
"""
Created on Tue May 28 14:36:46 2019

@author: Ruben
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statistics import mean, median


def execute_loop_and_save_iamges(data):
    for i in range(len(marcos)):
        
        marcoObjetivo = marcos[i] #'1D-15M_c'
    
    
        data['suma_direcciones'] = data['1D_direccion']+data['1H_direccion']
        
        fig, axs = plt.subplots(nrows=5, ncols=1, figsize=(7, 10))
        axs[0].set(ylabel='sum_direccs >= 5')
        axs[1].set(ylabel='sum_direccs = 4')
        axs[2].set(ylabel='sum_direccs = 3')
        axs[3].set(ylabel='sum_direccs = 2')
        axs[4].set(ylabel='sum_direccs = 1')
        
        sns.distplot(data[(data['color']=='verde') & (data['suma_direcciones']>=5)][marcoObjetivo], hist=False, color="g", kde_kws={"shade": True}, ax=axs[0])
        sns.distplot(data[(data['color']=='rojo') & (data['suma_direcciones']<=-5)][marcoObjetivo], hist=False, color="r", kde_kws={"shade": True}, ax=axs[0])
        sns.distplot(data[(data['color']=='verde') & (data['suma_direcciones']==4)][marcoObjetivo], hist=False, color="g", kde_kws={"shade": True}, ax=axs[1])
        sns.distplot(data[(data['color']=='rojo') & (data['suma_direcciones']==-4)][marcoObjetivo], hist=False, color="r", kde_kws={"shade": True}, ax=axs[1])
        sns.distplot(data[(data['color']=='verde') & (data['suma_direcciones']==3)][marcoObjetivo], hist=False, color="g", kde_kws={"shade": True}, ax=axs[2])
        sns.distplot(data[(data['color']=='rojo') & (data['suma_direcciones']==-3)][marcoObjetivo], hist=False, color="r", kde_kws={"shade": True}, ax=axs[2])
        sns.distplot(data[(data['color']=='verde') & (data['suma_direcciones']==2)][marcoObjetivo], hist=False, color="g", kde_kws={"shade": True}, ax=axs[3])
        sns.distplot(data[(data['color']=='rojo') & (data['suma_direcciones']==-2)][marcoObjetivo], hist=False, color="r", kde_kws={"shade": True}, ax=axs[3])
        sns.distplot(data[(data['color']=='verde') & (data['suma_direcciones']==1)][marcoObjetivo], hist=False, color="g", kde_kws={"shade": True}, ax=axs[4])
        sns.distplot(data[(data['color']=='rojo') & (data['suma_direcciones']==-1)][marcoObjetivo], hist=False, color="r", kde_kws={"shade": True}, ax=axs[4])
        
        meanG = data[(data['color']=='verde') & (data['suma_direcciones']>=5)][marcoObjetivo].mean()
        medianG = data[(data['color']=='verde') & (data['suma_direcciones']>=5)][marcoObjetivo].median()
        axs[0].axvline(meanG, color='g', linestyle='-')
        axs[0].axvline(medianG, color='g', linestyle='--')
        meanR = data[(data['color']=='rojo') & (data['suma_direcciones']<=-5)][marcoObjetivo].mean()
        medianR = data[(data['color']=='rojo') & (data['suma_direcciones']<=-5)][marcoObjetivo].median()
        axs[0].axvline(meanR, color='r', linestyle='-')
        axs[0].axvline(medianR, color='r', linestyle='--')
        
        meanG = data[(data['color']=='verde') & (data['suma_direcciones']==4)][marcoObjetivo].mean()
        medianG = data[(data['color']=='verde') & (data['suma_direcciones']==4)][marcoObjetivo].median()
        axs[1].axvline(meanG, color='g', linestyle='-')
        axs[1].axvline(medianG, color='g', linestyle='--')
        meanR = data[(data['color']=='rojo') & (data['suma_direcciones']==-4)][marcoObjetivo].mean()
        medianR = data[(data['color']=='rojo') & (data['suma_direcciones']==-4)][marcoObjetivo].median()
        axs[1].axvline(meanR, color='r', linestyle='-')
        axs[1].axvline(medianR, color='r', linestyle='--')
        
        meanG = data[(data['color']=='verde') & (data['suma_direcciones']==3)][marcoObjetivo].mean()
        medianG = data[(data['color']=='verde') & (data['suma_direcciones']==3)][marcoObjetivo].median()
        axs[2].axvline(meanG, color='g', linestyle='-')
        axs[2].axvline(medianG, color='g', linestyle='--')
        meanR = data[(data['color']=='rojo') & (data['suma_direcciones']==-3)][marcoObjetivo].mean()
        medianR = data[(data['color']=='rojo') & (data['suma_direcciones']==-3)][marcoObjetivo].median()
        axs[2].axvline(meanR, color='r', linestyle='-')
        axs[2].axvline(medianR, color='r', linestyle='--')
        
        meanG = data[(data['color']=='verde') & (data['suma_direcciones']==2)][marcoObjetivo].mean()
        medianG = data[(data['color']=='verde') & (data['suma_direcciones']==2)][marcoObjetivo].median()
        axs[3].axvline(meanG, color='g', linestyle='-')
        axs[3].axvline(medianG, color='g', linestyle='--')
        meanR = data[(data['color']=='rojo') & (data['suma_direcciones']==-2)][marcoObjetivo].mean()
        medianR = data[(data['color']=='rojo') & (data['suma_direcciones']==-2)][marcoObjetivo].median()
        axs[3].axvline(meanR, color='r', linestyle='-')
        axs[3].axvline(medianR, color='r', linestyle='--')
        
        meanG = data[(data['color']=='verde') & (data['suma_direcciones']==1)][marcoObjetivo].mean()
        medianG = data[(data['color']=='verde') & (data['suma_direcciones']==1)][marcoObjetivo].median()
        axs[4].axvline(meanG, color='g', linestyle='-')
        axs[4].axvline(medianG, color='g', linestyle='--')
        meanR = data[(data['color']=='rojo') & (data['suma_direcciones']==-1)][marcoObjetivo].mean()
        medianR = data[(data['color']=='rojo') & (data['suma_direcciones']==-1)][marcoObjetivo].median()
        axs[4].axvline(meanR, color='r', linestyle='-')
        axs[4].axvline(medianR, color='r', linestyle='--')
        
        fig.savefig(carpeta + "pred por suma direcciones " + nombresFicheros[i])
        plt.close(fig)


path = "tradingsim_2018eneroYfebrero_normalizadoPorVolatilidad.csv"
carpeta = "Graficos/2018 enero y febrero/"
nombresFicheros = ['01 15min','02 60min','03 mediodia','04 1Dentero','05 1D-15min']
marcos = ['15M_c','60M_c','mediodia','1D_c','1D-15M_c']


def main():
    data = pd.read_csv(path, sep=";")
    execute_loop_and_save_iamges(data)

if __name__ == "__main__":
   main()