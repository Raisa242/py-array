# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 19:54:27 2022

@author: Raisa
"""

from sklearn.cluster import AgglomerativeClustering 
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram,linkage

df=pd.read_csv("/Users/Raisa/PycharmProjects/stats_eda/heart.csv")
#df = mydata.mydata 
#df = mydata[ :, : ]
Z = linkage(df, method = "ward") 
dendro = dendrogram(Z) 
plt. title( 'Dendogram' ) 
plt.ylabel( 'Euclidean distance') 
plt. show()

ac = AgglomerativeClustering(n_clusters=2,affinity="euclidean", linkage="ward") 
labels = ac. fit_predict (df) 
plt. figure(figsize = (8,5) ) 
plt.scatter (df[labels == 0 ,0], df[labels == 0, 1] , c = 'red' )
plt.scatter (df [labels == 1 , 0] , df [labels == 1,1] , c = 'blue') 
plt.scatter (df [labels == 2 , 0], df [labels == 2 , 1],c = 'green' ) 
plt.scatter (df [labels == 3 , 0], df [ labels == 3 ,1],c = 'black') 
plt.scatter (df[labels == 4 ,] , df [ labels == 4 , 1], c = 'orange' ) 
plt. show()


