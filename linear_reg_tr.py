# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 21:26:39 2022

@author: Raisa
"""

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
from sklearn.metrics import r2_score,mean_squared_error
from sklearn import linear_model
from sklearn.model_selection import train_test_split

boston=load_boston()
x=pd.DataFrame(boston.data,columns=boston.feature_names)
y=pd.DataFrame(boston.target)
#splitting the data
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=4)
#creating the model
reg=linear_model.LinearRegression()
#fitting training data
reg.fit(x_train,y_train)
## Make predictions using the testing set
y_pred=reg.predict(x_test)
# The coefficients
print("Coefficients: \n", reg.coef_)
#r2 score
R=r2_score(y_test,y_pred)
print(R)
M=mean_squared_error(y_test,y_pred)
print(M)
plt.scatter(y_test,y_pred)
plt.xlabel("actual")
plt.ylabel("predicted")
plt.title("actual vs predicted")