# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 12:15:49 2019

@author: Ruben
"""

import pandas as pd

import chart_pred_por_direccion
import chart_pred_por_gap
import chart_pred_por_suma_direcciones
import chart_pred_por_tipo
import chart_pred_por_tipo_doble

charts = [chart_pred_por_direccion,
          chart_pred_por_gap,
          chart_pred_por_suma_direcciones,
          chart_pred_por_tipo,
          chart_pred_por_tipo_doble]

path = "tradingsim_todo_normalizadoPorVolatilidad.csv"
data = pd.read_csv(path, sep=";")
carpeta = "Graficos/todo/"

for chart in charts:
    chart.carpeta = carpeta
    chart.execute_loop_and_save_iamges(data)
    