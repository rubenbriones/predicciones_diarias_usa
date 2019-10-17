# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 14:29:24 2019

@author: Ruben
"""
import pandas as pd
import numpy as np

import analisis_estadistico.analisis_todos_los_filtros as ana

class DividirData():
    
    def __init__(self, data_org):
        self.data = data_org
        self.secciones = 1
        self.data_div = []
        
    def suflle(self):
        self.data = self.data.sample(frac=1, random_state=1)
        
    def dividir(self, weights):
        """
        :param weights: lista con los pesos que queremos dar a cada seccion,
                        en total todos los pesos deben sumar 1. ej: [0.4,0.4,0.2]
        """
        self.secciones = len(weights)
        self.data_div = []
        ini = 0
        for i in range(len(weights)):
            fin = int(len(self.data)*sum(weights[:i+1]))
            self.data_div.append(self.data.iloc[ini:fin])
            ini = fin

    def ejecutar_todos_filtros(self):
        if self.secciones == 1:
            res = ana.ejecutar_analisis(self.data)
            ana.save_results(res)
        else:
            for i in range(self.secciones):
                res = ana.ejecutar_analisis(self.data_div[i])
                ana.save_results(res, "sec"+str(i))


def main():
    path = "../data/tradingsim_todo_normalizadoPorVolatilidad.csv"
    data_org = pd.read_csv(path, sep=";")
    data_org['suma_direcciones'] = data_org['1D_direccion'] + data_org['1H_direccion']
    
    div = DividirData(data_org)
#    div.suflle()
#    div.dividir([0.4,0.4,0.2])
    div.dividir([0.33,0.33,0.34])
    div.ejecutar_todos_filtros()


if __name__ == "__main__":
   main()

