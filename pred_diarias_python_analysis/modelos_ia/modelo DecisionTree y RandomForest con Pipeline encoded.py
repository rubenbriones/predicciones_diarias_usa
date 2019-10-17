# -*- coding: utf-8 -*-
"""
Created on Thu May 30 13:37:28 2019

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
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder

path = "tradingsim_enero_normalizadoPorVolatilidad.csv"
data = pd.read_csv(path, sep=";")

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
X_train_full, X_valid_full, train_y, val_y = train_test_split(X, y, shuffle=False, random_state = 0)

# "Cardinality" means the number of unique values in a column
# Select categorical columns with relatively low cardinality (convenient but arbitrary)
categorical_cols = [cname for cname in X_train_full.columns if X_train_full[cname].nunique() < 10 and 
                        X_train_full[cname].dtype == "object"]

# Select numerical columns
numerical_cols = [cname for cname in X_train_full.columns if X_train_full[cname].dtype in ['int64', 'float64']]

# Keep selected columns only
my_cols = categorical_cols + numerical_cols
train_X = X_train_full[my_cols].copy()
val_X = X_valid_full[my_cols].copy()


# Preprocessing for numerical data - relleno los NaN de Gap con ceros
numerical_transformer = SimpleImputer(strategy='constant', fill_value=0)

# Preprocessing for categorical data
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

# Bundle preprocessing for numerical and categorical data
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, numerical_cols),
        ('cat', categorical_transformer, categorical_cols)
    ])






for max_leaf_nodes in [2,3,4,5,7,10,15,20,30,50,100,500,5000]:
    # Define model
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    # Bundle preprocessing and modeling code in a pipeline
    my_pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                                  ('model', model)])
    # Preprocessing of training data, fit model 
    my_pipeline.fit(train_X, train_y)    
    # Preprocessing of validation data, get predictions
    preds = my_pipeline.predict(val_X)    
    # Evaluate the model
    score = mean_absolute_error(val_y, preds)
    print("Max leaf nodes: %d  \t\t Mean Absolute Error:  %.4f" %(max_leaf_nodes, score))


print()
#AQUI ES LA PARTE DEL RANDOM FOREST
for n_estimators in [2,3,4,5,7,10,15,20,30,50,100,500,1000,5000]:
    model = RandomForestRegressor(n_estimators=n_estimators, random_state=1)
    my_pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                                  ('model', model)])
    my_pipeline.fit(train_X, train_y)    
    preds = my_pipeline.predict(val_X)   
    score = mean_absolute_error(val_y, preds)
    print("n_estimators: %d  \t\t Mean Absolute Error:  %.4f" %(n_estimators, score))
