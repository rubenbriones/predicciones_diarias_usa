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
        
        fig, axs = plt.subplots(nrows=4, ncols=2, figsize=(10, 9))
        axs[0,0].set(ylabel='direccion = 3')
        axs[1,0].set(ylabel='direccion = 2')
        axs[2,0].set(ylabel='direccion = 1')
        axs[3,0].set(ylabel='direccion = 0')
        
        sns.distplot(data[(data['color']=='verde') & (data['1D_direccion']==3)][marcoObjetivo], hist=False, color="g", kde_kws={"shade": True}, ax=axs[0,0])
        sns.distplot(data[(data['color']=='rojo') & (data['1D_direccion']==-3)][marcoObjetivo], hist=False, color="r", kde_kws={"shade": True}, ax=axs[0,0])
        sns.distplot(data[(data['color']=='verde') & (data['1D_direccion']==2)][marcoObjetivo], hist=False, color="g", kde_kws={"shade": True}, ax=axs[1,0])
        sns.distplot(data[(data['color']=='rojo') & (data['1D_direccion']==-2)][marcoObjetivo], hist=False, color="r", kde_kws={"shade": True}, ax=axs[1,0])
        sns.distplot(data[(data['color']=='verde') & (data['1D_direccion']==1)][marcoObjetivo], hist=False, color="g", kde_kws={"shade": True}, ax=axs[2,0])
        sns.distplot(data[(data['color']=='rojo') & (data['1D_direccion']==-1)][marcoObjetivo], hist=False, color="r", kde_kws={"shade": True}, ax=axs[2,0])
        sns.distplot(data[(data['color']=='verde') & (data['1D_direccion']==0)][marcoObjetivo], hist=False, color="g", kde_kws={"shade": True}, ax=axs[3,0])
        sns.distplot(data[(data['color']=='rojo') & (data['1D_direccion']==0)][marcoObjetivo], hist=False, color="r", kde_kws={"shade": True}, ax=axs[3,0])
        
        sns.distplot(data[(data['color']=='verde') & (data['1H_direccion']==3)][marcoObjetivo], hist=False, color="g", kde_kws={"shade": True}, ax=axs[0,1])
        sns.distplot(data[(data['color']=='rojo') & (data['1H_direccion']==-3)][marcoObjetivo], hist=False, color="r", kde_kws={"shade": True}, ax=axs[0,1])
        sns.distplot(data[(data['color']=='verde') & (data['1H_direccion']==2)][marcoObjetivo], hist=False, color="g", kde_kws={"shade": True}, ax=axs[1,1])
        sns.distplot(data[(data['color']=='rojo') & (data['1H_direccion']==-2)][marcoObjetivo], hist=False, color="r", kde_kws={"shade": True}, ax=axs[1,1])
        sns.distplot(data[(data['color']=='verde') & (data['1H_direccion']==1)][marcoObjetivo], hist=False, color="g", kde_kws={"shade": True}, ax=axs[2,1])
        sns.distplot(data[(data['color']=='rojo') & (data['1H_direccion']==-1)][marcoObjetivo], hist=False, color="r", kde_kws={"shade": True}, ax=axs[2,1])
        sns.distplot(data[(data['color']=='verde') & (data['1H_direccion']==0)][marcoObjetivo], hist=False, color="g", kde_kws={"shade": True}, ax=axs[3,1])
        sns.distplot(data[(data['color']=='rojo') & (data['1H_direccion']==0)][marcoObjetivo], hist=False, color="r", kde_kws={"shade": True}, ax=axs[3,1])
        
        meanG = data[(data['color']=='verde') & (data['1D_direccion']==3)][marcoObjetivo].mean()
        medianG = data[(data['color']=='verde') & (data['1D_direccion']==3)][marcoObjetivo].median()
        axs[0,0].axvline(meanG, color='g', linestyle='-')
        axs[0,0].axvline(medianG, color='g', linestyle='--')
        meanR = data[(data['color']=='rojo') & (data['1D_direccion']==-3)][marcoObjetivo].mean()
        medianR = data[(data['color']=='rojo') & (data['1D_direccion']==-3)][marcoObjetivo].median()
        axs[0,0].axvline(meanR, color='r', linestyle='-')
        axs[0,0].axvline(medianR, color='r', linestyle='--')
        
        meanG = data[(data['color']=='verde') & (data['1D_direccion']==2)][marcoObjetivo].mean()
        medianG = data[(data['color']=='verde') & (data['1D_direccion']==2)][marcoObjetivo].median()
        axs[1,0].axvline(meanG, color='g', linestyle='-')
        axs[1,0].axvline(medianG, color='g', linestyle='--')
        meanR = data[(data['color']=='rojo') & (data['1D_direccion']==-2)][marcoObjetivo].mean()
        medianR = data[(data['color']=='rojo') & (data['1D_direccion']==-2)][marcoObjetivo].median()
        axs[1,0].axvline(meanR, color='r', linestyle='-')
        axs[1,0].axvline(medianR, color='r', linestyle='--')
        
        meanG = data[(data['color']=='verde') & (data['1D_direccion']==1)][marcoObjetivo].mean()
        medianG = data[(data['color']=='verde') & (data['1D_direccion']==1)][marcoObjetivo].median()
        axs[2,0].axvline(meanG, color='g', linestyle='-')
        axs[2,0].axvline(medianG, color='g', linestyle='--')
        meanR = data[(data['color']=='rojo') & (data['1D_direccion']==-1)][marcoObjetivo].mean()
        medianR = data[(data['color']=='rojo') & (data['1D_direccion']==-1)][marcoObjetivo].median()
        axs[2,0].axvline(meanR, color='r', linestyle='-')
        axs[2,0].axvline(medianR, color='r', linestyle='--')
        
        meanG = data[(data['color']=='verde') & (data['1D_direccion']==0)][marcoObjetivo].mean()
        medianG = data[(data['color']=='verde') & (data['1D_direccion']==0)][marcoObjetivo].median()
        axs[3,0].axvline(meanG, color='g', linestyle='-')
        axs[3,0].axvline(medianG, color='g', linestyle='--')
        meanR = data[(data['color']=='rojo') & (data['1D_direccion']==0)][marcoObjetivo].mean()
        medianR = data[(data['color']=='rojo') & (data['1D_direccion']==0)][marcoObjetivo].median()
        axs[3,0].axvline(meanR, color='r', linestyle='-')
        axs[3,0].axvline(medianR, color='r', linestyle='--')
        
        
        meanG = data[(data['color']=='verde') & (data['1H_direccion']==3)][marcoObjetivo].mean()
        medianG = data[(data['color']=='verde') & (data['1H_direccion']==3)][marcoObjetivo].median()
        axs[0,1].axvline(meanG, color='g', linestyle='-')
        axs[0,1].axvline(medianG, color='g', linestyle='--')
        meanR = data[(data['color']=='rojo') & (data['1H_direccion']==-3)][marcoObjetivo].mean()
        medianR = data[(data['color']=='rojo') & (data['1H_direccion']==-3)][marcoObjetivo].median()
        axs[0,1].axvline(meanR, color='r', linestyle='-')
        axs[0,1].axvline(medianR, color='r', linestyle='--')
        
        meanG = data[(data['color']=='verde') & (data['1H_direccion']==2)][marcoObjetivo].mean()
        medianG = data[(data['color']=='verde') & (data['1H_direccion']==2)][marcoObjetivo].median()
        axs[1,1].axvline(meanG, color='g', linestyle='-')
        axs[1,1].axvline(medianG, color='g', linestyle='--')
        meanR = data[(data['color']=='rojo') & (data['1H_direccion']==-2)][marcoObjetivo].mean()
        medianR = data[(data['color']=='rojo') & (data['1H_direccion']==-2)][marcoObjetivo].median()
        axs[1,1].axvline(meanR, color='r', linestyle='-')
        axs[1,1].axvline(medianR, color='r', linestyle='--')
        
        meanG = data[(data['color']=='verde') & (data['1H_direccion']==1)][marcoObjetivo].mean()
        medianG = data[(data['color']=='verde') & (data['1H_direccion']==1)][marcoObjetivo].median()
        axs[2,1].axvline(meanG, color='g', linestyle='-')
        axs[2,1].axvline(medianG, color='g', linestyle='--')
        meanR = data[(data['color']=='rojo') & (data['1H_direccion']==-1)][marcoObjetivo].mean()
        medianR = data[(data['color']=='rojo') & (data['1H_direccion']==-1)][marcoObjetivo].median()
        axs[2,1].axvline(meanR, color='r', linestyle='-')
        axs[2,1].axvline(medianR, color='r', linestyle='--')
        
        meanG = data[(data['color']=='verde') & (data['1H_direccion']==0)][marcoObjetivo].mean()
        medianG = data[(data['color']=='verde') & (data['1H_direccion']==0)][marcoObjetivo].median()
        axs[3,1].axvline(meanG, color='g', linestyle='-')
        axs[3,1].axvline(medianG, color='g', linestyle='--')
        meanR = data[(data['color']=='rojo') & (data['1H_direccion']==0)][marcoObjetivo].mean()
        medianR = data[(data['color']=='rojo') & (data['1H_direccion']==0)][marcoObjetivo].median()
        axs[3,1].axvline(meanR, color='r', linestyle='-')
        axs[3,1].axvline(medianR, color='r', linestyle='--')
        
        fig.savefig(carpeta + "pred por direccion " + nombresFicheros[i])
        plt.close(fig)
        

path = "tradingsim_2018eneroYfebrero_normalizadoPorVolatilidad.csv"
carpeta = "Graficos/2018 enero y febrero22/"
nombresFicheros = ['01 15min','02 60min','03 mediodia','04 1Dentero','05 1D-15min']
marcos = ['15M_c','60M_c','mediodia','1D_c','1D-15M_c']


def main():
    data = pd.read_csv(path, sep=";")
    execute_loop_and_save_iamges(data)

if __name__ == "__main__":
   main()