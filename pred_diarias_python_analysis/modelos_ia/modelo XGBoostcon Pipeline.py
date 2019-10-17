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
from sklearn.model_selection import cross_val_score
from xgboost import XGBRegressor

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


n_estimators=1000
learning_rate=0.05
early_stopping_rounds=5
model = XGBRegressor(n_estimators=n_estimators, learning_rate=learning_rate, n_jobs=4)

my_pipeline = Pipeline(steps=[('preprocessor', preprocessor), 
                              ('m', model)])

my_pipeline.fit(train_X, train_y,
                m__early_stopping_rounds=early_stopping_rounds,
                m__eval_set=[(val_X, val_y)])

#my_pipeline.fit(train_X, train_y)

my_pipeline
preds = my_pipeline.predict(val_X)
score = mean_absolute_error(val_y, preds)
print("Estimators/LearningRate/StopRounds: %d/%.2f/%d \t\t Mean Absolute Error:  %.4f" 
      %(n_estimators, learning_rate, early_stopping_rounds, score))
    
