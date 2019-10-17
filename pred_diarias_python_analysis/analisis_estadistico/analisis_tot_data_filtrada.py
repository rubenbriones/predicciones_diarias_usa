# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 18:36:23 2019

@author: Ruben
"""

import pandas as pd
import numpy as np
import scipy
import matplotlib.pyplot as plt
import seaborn as sns

_etiqueta_groupby = 'stock'
_marcos = ['15M_c','60M_c','mediodia','1D_c','1D-15M_c']
_marcos_x_lim = [.75, 1.25, 1.75, 2, 2]

def set_marcos(marcos, marcos_x_lim):
    global _marcos, _marcos_x_lim
    _marcos = marcos
    _marcos_x_lim = marcos_x_lim

def obtener_resultados_globales(data, mostrar_graficos):    
    areas = mostrar_graficos_del_data_filtrado(data, mostrar_graficos)        
    
    data.loc[data.color=='rojo', _marcos] *= -1
    grouped = data.groupby([_etiqueta_groupby, 'color'])
    res = grouped[_marcos].agg([np.sum])
    res = res.round(2)
    #islc = pd.IndexSlice
    #res.loc[islc[:, 'rojo'], :] *= -1
    res_conj = res.sum(level=0)
    res_conj['num_preds'] = data.groupby(_etiqueta_groupby).size()
    
    res_conj_d = pd.DataFrame(columns=res_conj.columns)
    res_conj_d.loc["-"] = ["-" for i in res_conj_d.columns]
    porc_acierto_ind = (data[_marcos].gt(0).sum()/len(data)).round(2)
    porc_acierto_ind.index = pd.MultiIndex.from_product([porc_acierto_ind.index, ['sum']])
    res_conj_d.loc["% ind>0"] = porc_acierto_ind
    res_conj_d.loc["% sum>0"] = (res_conj.gt(0).sum()/len(res_conj)).round(2)
    res_conj_d.loc["totSum/N"] = (res_conj.sum()/res_conj['num_preds'].sum()).round(2)
    res_conj_d.loc["Total"] = res_conj.sum()
    res_conj_d.loc["--"] = ["-" for i in res_conj_d.columns]
    res_conj_d = res_conj_d.append(areas)[res_conj_d.columns.tolist()]
    
    if mostrar_graficos:
        print(pd.concat([res_conj, res_conj_d]))
        
    return res_conj_d

def mostrar_graficos_del_data_filtrado(data, mostrar_graficos):
    areas = pd.DataFrame(columns=[(m, 'sum') for m in _marcos])
    fig, axs = plt.subplots(nrows=len(_marcos), ncols=1, figsize=(5, 2.5*len(_marcos)))
        
    for i, m in enumerate(_marcos):
        axs[i].set(ylabel=m)
        axs[i].set_xlim(-_marcos_x_lim[i],_marcos_x_lim[i])
        sns.distplot(data[data['color']=='verde'][m], hist=False, color="g", kde_kws={"shade": True}, ax=axs[i])
        sns.distplot(data[data['color']=='rojo'][m], hist=False, color="r", kde_kws={"shade": True}, ax=axs[i])
        
        meanG = data[data['color']=='verde'][m].mean()
        medianG = data[data['color']=='verde'][m].median()
        axs[i].axvline(meanG, color='g', linestyle='-')
        axs[i].axvline(medianG, color='g', linestyle='--')
        meanR = data[data['color']=='rojo'][m].mean()
        medianR = data[data['color']=='rojo'][m].median()
        axs[i].axvline(meanR, color='r', linestyle='-')
        axs[i].axvline(medianR, color='r', linestyle='--')
        
        #Get the data from the KDE line
        xdata_v, ydata_v = axs[i].get_lines()[0].get_data()
        xdata_r, ydata_r = axs[i].get_lines()[1].get_data()
        
        #Generate new set of datas (based on functions) but with the same X values
        xdata_inter = np.linspace(-5,5,500)
        ydata_v_interp = np.zeros(xdata_inter.shape)
        ydata_r_interp = np.zeros(xdata_inter.shape)
        ydata_zeros = np.zeros(xdata_inter.shape)
        for i, x in enumerate(xdata_inter):
            #Find the closest point on the curve
            idx_v = (np.abs(xdata_v-x)).argmin()
            idx_r = (np.abs(xdata_r-x)).argmin()
            #Interpolate to get a better estimate
            ydata_v_interp[i] = np.interp(x,xdata_v[idx_v:idx_v+2],ydata_v[idx_v:idx_v+2])
            ydata_r_interp[i] = np.interp(x,xdata_r[idx_r:idx_r+2],ydata_r[idx_r:idx_r+2])

        #Find the function by integrating the points
        #f_v = scipy.integrate.cumtrapz(ydata_v, xdata_v, initial=0)
        #f_r = scipy.integrate.cumtrapz(ydata_r, xdata_r, initial=0)
        
        #The area between two curvesis simply the difference between the area under f(x) and the area under g(x)
        #And this can be calculated with a definite integral. 
        #area_tot_array = scipy.integrate.cumtrapz(ydata_v_interp-ydata_r_interp, xdata_inter)
        #area_tot = scipy.integrate.trapz(ydata_v_interp - ydata_r_interp,
        #                                 xdata_inter)
        #areas.loc["dif area tot", (m, 'sum')] = np.round(area_tot, 3)
        
        #Aqui calculamos el area del verde que esta en en lado positivo,
        #y el area del rojo que esta en el lado negativo ("positivo" realmente pues serian posiciones cortas)
        area_v_pos = scipy.integrate.trapz(ydata_v_interp[len(ydata_v_interp)//2:] - ydata_zeros[len(ydata_zeros)//2:], 
                                           xdata_inter[len(xdata_inter)//2:])
        area_r_neg = scipy.integrate.trapz(ydata_r_interp[:len(ydata_r_interp)//2] - ydata_zeros[:len(ydata_zeros)//2], 
                                           xdata_inter[:len(xdata_inter)//2])
        areas.loc["area verde pos", (m, 'sum')] = np.round(area_v_pos, 2)
        areas.loc["area roja neg", (m, 'sum')] = np.round(area_r_neg, 2)
        areas.loc["suma alfas areas", (m, 'sum')] = np.round(area_v_pos-0.5 + area_r_neg-0.5, 2)
        
        #Aqui calculamos la diferencia de las curvas en el lado positivo y negativo por separado
        area_pos = scipy.integrate.trapz(ydata_v_interp[len(ydata_v_interp)//2:] - ydata_r_interp[len(ydata_r_interp)//2:], 
                                         xdata_inter[len(xdata_inter)//2:])
        area_neg = scipy.integrate.trapz(ydata_v_interp[:len(ydata_v_interp)//2] - ydata_r_interp[:len(ydata_r_interp)//2], 
                                         xdata_inter[:len(xdata_inter)//2])
        #areas.loc["dif area pos", (m, 'sum')] = np.round(area_pos, 2)
        #areas.loc["dif area neg", (m, 'sum')] = np.round(area_neg, 2)
        areas.loc["dif area pos-neg", (m, 'sum')] = np.round(area_pos - area_neg, 2)
    
    if mostrar_graficos:
        plt.plot()
    else:
        plt.close(fig)
    return areas


def main():
    path = "../data/tradingsim_todo_normalizadoPorVolatilidad.csv"
    data_org = pd.read_csv(path, sep=";")
    
    #AQUI FILTRAMOS LA data_org
    #data = data_org[['stock','color']+_marcos]
    data = data_org.loc[abs(data_org['1H_direccion']).isin([3]), [_etiqueta_groupby,'color']+_marcos]
    #data = data_org.loc[data_org['1H_tipo'].isin(['A']), ['stock','color']+_marcos]
    
    res_conj_d = obtener_resultados_globales(data, True)

if __name__ == "__main__":
   main()