# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 07:48:25 2019

@author: Ruben
"""

from datetime import datetime
import pandas as pd
import pickle
import analisis_estadistico.analisis_tot_data_filtrada as ana

marcos = ['15M_c','60M_c','mediodia','1D_c','1D-15M_c']
marcos_x_lim = [.75, 1.25, 1.75, 2, 2]

#los filtros de tipo gap se aplicarian por encima de los filtros normales
#para ser un primer filtrado de que si directamente la accion abre en la apertura
#a un precio que no nos interesa pues directamente descartamos la operacion
filtros_gap =[['sin filt_gap', lambda d: d['stock']!='']] #ej: lambda d: abs(d['gap'])<=lim

filtros = [['sin filtro', lambda d: d['stock']!=''],
           ['1D_d=3,2', lambda d: abs(d['1D_direccion']).isin([3,2])],
           ['1D_d=3', lambda d: abs(d['1D_direccion']).isin([3])],
           ['1D_d=2', lambda d: abs(d['1D_direccion']).isin([2])],
           ['1D_d=1', lambda d: abs(d['1D_direccion']).isin([1])],
           ['1D_d=0', lambda d: abs(d['1D_direccion']).isin([0])],
           ['1D_d=1,0', lambda d: abs(d['1D_direccion']).isin([1,0])],
           
           ['1H_d=3,2', lambda d: abs(d['1H_direccion']).isin([3,2])],
           ['1H_d=3', lambda d: abs(d['1H_direccion']).isin([3])],
           ['1H_d=2', lambda d: abs(d['1H_direccion']).isin([2])],
           ['1H_d=1', lambda d: abs(d['1H_direccion']).isin([1])],
           ['1H_d=0', lambda d: abs(d['1H_direccion']).isin([0])],
           ['1H_d=1,0', lambda d: abs(d['1H_direccion']).isin([1,0])],
           
           ['sum_d=6,5', lambda d: abs(d['suma_direcciones']).isin([6,5])],
           ['sum_d=6', lambda d: abs(d['suma_direcciones']).isin([6])],
           ['sum_d=5', lambda d: abs(d['suma_direcciones']).isin([5])],
           ['sum_d=4', lambda d: abs(d['suma_direcciones']).isin([4])],
           ['sum_d=3', lambda d: abs(d['suma_direcciones']).isin([3])],
           ['sum_d=2', lambda d: abs(d['suma_direcciones']).isin([2])],
           ['sum_d=1', lambda d: abs(d['suma_direcciones']).isin([1])],
           
           ['1D_t=P', lambda d: d['1D_tipo'].isin(['P'])],
           ['1D_t=N', lambda d: d['1D_tipo'].isin(['N'])],
           ['1D_t=A', lambda d: d['1D_tipo'].isin(['A'])],
           
           ['1H_t=P', lambda d: d['1H_tipo'].isin(['P'])],
           ['1H_t=N', lambda d: d['1H_tipo'].isin(['N'])],
           ['1H_t=A', lambda d: d['1H_tipo'].isin(['A'])],
           
           ['1D&1H_t=P', lambda d: d['1D_tipo'].isin(['P']) & d['1H_tipo'].isin(['P'])],
           ['1D&1H_t=A', lambda d: d['1D_tipo'].isin(['A']) & d['1H_tipo'].isin(['A'])]]

def ejecutar_analisis(data_org):
    res = []
    for f_gap in filtros_gap:
        data_f_gap = data_org.loc[f_gap[1](data_org)]
        for f in filtros:            
            data_filt = data_f_gap.loc[f[1](data_f_gap), ['stock','color']+marcos]
            res_conj_d = ana.obtener_resultados_globales(data_filt, False)
            res.append((f_gap[0]+' & '+f[0], res_conj_d))
    return res

def save_results(res, nombre_extra=""):
    res_sort = sorted(res, key = lambda e: e[1].loc['Total'][:-1].sum(), reverse=True)
    
    for e in res_sort:
        print(e[0])
    
    fecha = datetime.now().strftime("%Y%m%d_%H%M%S") + nombre_extra
    
    with open('../Analisis resultados/'+fecha+'_object_res.txt', 'wb') as f:
        pickle.dump(res, f)
    with open('../Analisis resultados/'+fecha+'_excel.txt', 'w') as f:
        for e in res_sort:
            f.write(e[0]+'\t'+
                    e[1].loc[['Total']].to_string(header=False).replace('.',',')+' '+
                    e[1].loc[['area verde pos']].to_string(header=False).replace('.',',')+' '+
                    e[1].loc[['area roja neg']].to_string(header=False).replace('.',',')+' '+
                    e[1].loc[['suma alfas areas']].to_string(header=False).replace('.',',')+' '+
                    e[1].loc[['dif area pos-neg']].to_string(header=False).replace('.',',')+'\n')
    with open('../Analisis resultados/'+fecha+'.txt', 'w') as f:
        for e in res:
            f.write(e[0]+'\n')
            f.write(e[1].iloc[1:].to_string()+'\n\n')
    with open('../Analisis resultados/'+fecha+'_sorted.txt', 'w') as f:
        for e in res_sort:
            f.write(e[0]+'\n')
            f.write(e[1].iloc[1:].to_string()+'\n\n')
    
def main():
    path = "../data/tradingsim_todo_normalizadoPorVolatilidad.csv"
    data_org = pd.read_csv(path, sep=";")
    data_org['suma_direcciones'] = data_org['1D_direccion'] + data_org['1H_direccion']
    
    res = ejecutar_analisis(data_org)
    
    save_results(res)
    
if __name__ == "__main__":
   main()
   
   
def read_res_object():
    nombre_fichero = '20190712_095528_object_res'
    with open('Analisis resultados/'+nombre_fichero+'.txt', 'rb') as f:
        res = pickle.load(f)
    
    res_sort = sorted(res, key = lambda e: e[1].loc['Total'][:-1].sum(), reverse=True)
    
    with open('Analisis resultados/'+nombre_fichero+'_excel.txt', 'w') as f:
        for e in res_sort:
            f.write(e[0]+'\t'+
                    e[1].loc[['Total']].to_string(header=False).replace('.',',')+' '+
                    e[1].loc[['area verde pos']].to_string(header=False).replace('.',',')+' '+
                    e[1].loc[['area roja neg']].to_string(header=False).replace('.',',')+' '+
                    e[1].loc[['suma alfas areas']].to_string(header=False).replace('.',',')+' '+
                    e[1].loc[['dif area pos-neg']].to_string(header=False).replace('.',',')+'\n')

