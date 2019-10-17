# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 12:15:49 2019

@author: Ruben
"""

import pandas as pd
import itertools
import os

import chart_pred_por_direccion
import chart_pred_por_gap
import chart_pred_por_suma_direcciones
import chart_pred_por_tipo
import chart_pred_por_tipo_doble


def apply_sl_and_pf(data, sl, pf):
    marcos = ['15M','60M','1D','1D-15M']
    for idx, row in data.iterrows():
        for m in marcos:
            if row['color'] == 'verde':
                data.loc[idx, m+'_c'] = sl if row[m+'_min'] <= sl else pf if row[m+'_max'] >= pf else row[m+'_c']
            else: #color=rojo
                data.loc[idx, m+'_c'] = -sl if row[m+'_max'] >= -sl else -pf if row[m+'_min'] <= -pf else row[m+'_c']
    return data 


charts = [chart_pred_por_direccion,
          chart_pred_por_gap,
          chart_pred_por_suma_direcciones,
          chart_pred_por_tipo,
          chart_pred_por_tipo_doble]

path = "tradingsim_todo_normalizadoPorVolatilidad.csv"
data = pd.read_csv(path, sep=";")
carpeta = "Graficos/todo_SL_PF/"
    
stops = [0.5,1,2,3] #[0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 2, 2.5, 3]
profs = [0.5,1,2,3] #[0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 2, 2.5, 3]
stops = [-x for x in stops]
combs = list(itertools.product(stops, profs))
combs_str = ['(sl,pf)='+str(x) for x in combs]

for c in combs:
    sl = c[0]
    pf = c[1]
    data_with_sl_pf = apply_sl_and_pf(data.copy(deep=True), sl, pf)
    
    for chart in charts:
        chart.carpeta = carpeta+'(sl,pf)='+str(c)+'/'
        if not os.path.exists(chart.carpeta):
            os.makedirs(chart.carpeta)
        chart.execute_loop_and_save_iamges(data_with_sl_pf)
        