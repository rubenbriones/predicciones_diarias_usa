# -*- coding: utf-8 -*-
"""
Created on Thu May 30 10:55:00 2019

@author: Ruben
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statistics import mean, median
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder

path = "tradingsim_enero_normalizadoPorVolatilidad.csv"
data = pd.read_csv(path, sep=";")

data['gap']=data['gap'].fillna(0)

data['suma_direcciones'] = data['1D_direccion']+data['1H_direccion']
data['60m-15m'] = data['60M_c']-data['15M_c']
data['mediodia-15m'] = data['mediodia']-data['15M_c']
data['1dia-15m'] = data['1D_c']-data['15M_c'] #esta col sera muy parecida a la de 1D-15M_c
data['mediodia-60m'] = data['mediodia']-data['60M_c']
data['1dia-60m'] = data['1D_c']-data['60M_c']



# Choose target and features
y = data['15M_c']
features = ['gap', '1D_tipo', '1H_tipo', 'color']
X = data[features]


# split data into training and validation data, for both features and target
# The split is based on a random number generator. Supplying a numeric value to
# the random_state argument guarantees we get the same split every time we
# run this script.
train_X, val_X, train_y, val_y = train_test_split(X, y, shuffle=False, random_state = 0)


#One-hot encode categorical variables
s = (train_X.dtypes == object)
text_cols = list(s[s].index)
OH_encoder = OneHotEncoder(handle_unknown='ignore', sparse=False)
OH_cols_train = pd.DataFrame(OH_encoder.fit_transform(train_X[text_cols]))
OH_cols_valid = pd.DataFrame(OH_encoder.transform(val_X[text_cols]))

# One-hot encoding removed index; put it back
OH_cols_train.index = train_X.index
OH_cols_valid.index = val_X.index

# Remove categorical columns (will replace with one-hot encoding)
soloNums_X_train = train_X.drop(text_cols, axis=1)
soloNums_X_valid = val_X.drop(text_cols, axis=1)

# Add one-hot encoded columns to numerical features
OH_X_train = pd.concat([soloNums_X_train, OH_cols_train], axis=1)
OH_X_valid = pd.concat([soloNums_X_valid, OH_cols_valid], axis=1)


for max_leaf_nodes in [2,3,4,5,7,10,15,20,30,50,100,500,5000]:
    # Define model
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    # Fit model
    model.fit(OH_X_train, train_y)
    # get predicted prices on validation data
    val_predictions = model.predict(OH_X_valid)
    my_mae = mean_absolute_error(val_y, val_predictions)
    #print(my_mae)
    #for i, pred in enumerate(val_predictions): print("{:.2f} {:.2f}".format(y[i], pred).replace('.',','))
    
    print("Max leaf nodes: %d  \t\t Mean Absolute Error:  %.4f" %(max_leaf_nodes, my_mae))


print()
#AQUI ES LA PARTE DEL RANDOM FOREST
for n_estimators in [2,3,4,5,7,10,15,20,30,50,100,500,1000,5000]:
    model = RandomForestRegressor(n_estimators=n_estimators, random_state=1)
    model.fit(OH_X_train, train_y)
    val_predictions = model.predict(OH_X_valid)
    my_mae = mean_absolute_error(val_y, val_predictions)
    print("n_estimators: %d  \t\t Mean Absolute Error:  %.4f" %(n_estimators, my_mae))

