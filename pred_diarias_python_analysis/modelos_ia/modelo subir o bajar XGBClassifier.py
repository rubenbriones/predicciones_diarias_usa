# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 18:58:44 2019

@author: Ruben
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statistics import mean, median
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder
from xgboost import XGBClassifier

def calcularGanancias_binario(model, cols_X, col_y_ganancias):
    val_pred = model.predict(cols_X)
    aux = pd.Series(val_pred, index=OH_X_valid.index)
    aux = pd.concat([aux, col_y_ganancias], axis=1, join='inner')
    gananciasAlcistas = aux.iloc[:,1][aux.iloc[:,0]==True].sum() #de la columna[1]=(col_y_ganancias) selecciono solo aquellos valores que su prediccin fue ALZA[true]
    gananciasBajistas = -1*aux.iloc[:,1][aux.iloc[:,0]==False].sum()
    return gananciasAlcistas+gananciasBajistas


path = "../tradingsim_2018enero_normalizadoPorVolatilidad.csv"
data = pd.read_csv(path, sep=";")

data['gap']=data['gap'].fillna(0)

data['suma_direcciones'] = data['1D_direccion']+data['1H_direccion']
data['60m-15m'] = data['60M_c']-data['15M_c']
data['mediodia-15m'] = data['mediodia']-data['15M_c']
data['1dia-15m'] = data['1D_c']-data['15M_c'] #esta col sera muy parecida a la de 1D-15M_c
data['mediodia-60m'] = data['mediodia']-data['60M_c']
data['1dia-60m'] = data['1D_c']-data['60M_c']


data['15M_c_binario'] = data['15M_c']>0
data['60M_c_binario'] = data['60M_c']>0
data['mediodia_binario'] = data['mediodia']>0
data['1D_c_binario'] = data['1D_c']>0
data['1D-15M_c_binario'] = data['1D-15M_c']>0


# Choose target and features
y = data['1D-15M_c_binario']
features = ['1H_tipo', '1H_direccion', '15M_c' ]
X = data[features]


# split data into training and validation data, for both features and target
# The split is based on a random number generator. Supplying a numeric value to
# the random_state argument guarantees we get the same split every time we
# run this script.
train_X, val_X, train_y, val_y = train_test_split(X, y, shuffle=False, random_state = 0)


#One-hot encode categorical variables
s = (train_X.dtypes == object)
if s.sum() > 0:
    text_cols = list(s[s].index)
    OH_encoder = OneHotEncoder(handle_unknown='ignore', sparse=False)
    OH_cols_train = pd.DataFrame(OH_encoder.fit_transform(train_X[text_cols]))
    OH_cols_valid = pd.DataFrame(OH_encoder.transform(val_X[text_cols]))
    OH_cols_train.columns = OH_encoder.get_feature_names()
    OH_cols_valid.columns = OH_encoder.get_feature_names()
    
    # One-hot encoding removed index; put it back
    OH_cols_train.index = train_X.index
    OH_cols_valid.index = val_X.index
    
    # Remove categorical columns (will replace with one-hot encoding)
    soloNums_X_train = train_X.drop(text_cols, axis=1)
    soloNums_X_valid = val_X.drop(text_cols, axis=1)
    
    # Add one-hot encoded columns to numerical features
    OH_X_train = pd.concat([soloNums_X_train, OH_cols_train], axis=1)
    OH_X_valid = pd.concat([soloNums_X_valid, OH_cols_valid], axis=1)
else:
    OH_X_train = train_X
    OH_X_valid = val_X




n_estimators=1000
learning_rate=0.05
early_stopping_rounds=20
my_model = XGBClassifier(n_estimators=n_estimators, learning_rate=learning_rate, n_jobs=4)

my_model.fit(OH_X_train, train_y, 
             early_stopping_rounds=early_stopping_rounds, 
             eval_set=[(OH_X_valid, val_y)], 
             verbose=False)


val_predictions = my_model.predict(OH_X_valid)

print(pd.Series(my_model.feature_importances_, index=OH_X_valid.columns))
score = my_model.score(X=OH_X_valid, y=val_y) #esto es el % de aciertos
print("Estimators/LearningRate/StopRounds: %d/%.2f/%d \t Score:  %.4f" 
      %(n_estimators, learning_rate, early_stopping_rounds, score))

print(calcularGanancias_binario(model=my_model, 
                                cols_X=OH_X_valid, 
                                col_y_ganancias=data['1D-15M_c']))


    


####### ESTO ES PARA COMPROBAR CON EL MES DE FEBRERO SI FUNCIONO ######
#path = "../tradingsim_2018febrero_normalizadoPorVolatilidad.csv"
#data = pd.read_csv(path, sep=";")
#
#data['gap']=data['gap'].fillna(0)
#
#data['suma_direcciones'] = data['1D_direccion']+data['1H_direccion']
#data['60m-15m'] = data['60M_c']-data['15M_c']
#data['mediodia-15m'] = data['mediodia']-data['15M_c']
#data['1dia-15m'] = data['1D_c']-data['15M_c'] #esta col sera muy parecida a la de 1D-15M_c
#data['mediodia-60m'] = data['mediodia']-data['60M_c']
#data['1dia-60m'] = data['1D_c']-data['60M_c']
#
#
#data['15M_c_binario'] = data['15M_c']>0
#data['60M_c_binario'] = data['60M_c']>0
#data['mediodia_binario'] = data['mediodia']>0
#data['1D_c_binario'] = data['1D_c']>0
#data['1D-15M_c_binario'] = data['1D-15M_c']>0
#
#
## Choose target and features
#y = data['1D-15M_c_binario']
#features = ['1H_tipo', '1H_direccion', '15M_c' ]
#X = data[features]
#
#
## split data into training and validation data, for both features and target
## The split is based on a random number generator. Supplying a numeric value to
## the random_state argument guarantees we get the same split every time we
## run this script.
#train_X, val_X, train_y, val_y = train_test_split(X, y, test_size=0.9, shuffle=False, random_state = 0)
#
#
##One-hot encode categorical variables
#s = (train_X.dtypes == object)
#if s.sum() > 0:
#    text_cols = list(s[s].index)
#    OH_encoder = OneHotEncoder(handle_unknown='ignore', sparse=False)
#    OH_cols_train = pd.DataFrame(OH_encoder.fit_transform(train_X[text_cols]))
#    OH_cols_valid = pd.DataFrame(OH_encoder.transform(val_X[text_cols]))
#    OH_cols_train.columns = OH_encoder.get_feature_names()
#    OH_cols_valid.columns = OH_encoder.get_feature_names()
#    
#    # One-hot encoding removed index; put it back
#    OH_cols_train.index = train_X.index
#    OH_cols_valid.index = val_X.index
#    
#    # Remove categorical columns (will replace with one-hot encoding)
#    soloNums_X_train = train_X.drop(text_cols, axis=1)
#    soloNums_X_valid = val_X.drop(text_cols, axis=1)
#    
#    # Add one-hot encoded columns to numerical features
#    OH_X_train = pd.concat([soloNums_X_train, OH_cols_train], axis=1)
#    OH_X_valid = pd.concat([soloNums_X_valid, OH_cols_valid], axis=1)
#else:
#    OH_X_train = train_X
#    OH_X_valid = val_X
#
#OH_X_valid['x0_N']=0
#OH_X_valid=OH_X_valid[['1H_direccion', '15M_c', 'x0_A', 'x0_N', 'x0_P']]
#val_predictions = my_model.predict(OH_X_valid)
#
#
#print(pd.Series(my_model.feature_importances_, index=OH_X_valid.columns))
#score = my_model.score(X=OH_X_valid, y=val_y) #esto es el % de aciertos
#print("Estimators/LearningRate/StopRounds: %d/%.2f/%d \t Score:  %.4f" 
#      %(n_estimators, learning_rate, early_stopping_rounds, score))
#
#print(calcularGanancias_binario(model=my_model, 
#                                cols_X=OH_X_valid, 
#                                col_y_ganancias=data['1D-15M_c']))