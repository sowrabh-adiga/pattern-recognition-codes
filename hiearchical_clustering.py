# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
'''
X = np.array([[0.0,0.0],
              [0.5,0.0],
              [0.0,2.0],
              [2.0,2.0],
              [2.5,8.0],
              [6.0,3.0],
              [7.0,3.0]])

from sklearn.cluster import AgglomerativeClustering

cluster = AgglomerativeClustering(n_clusters=2,affinity='euclidean',linkage='single')
cluster.fit_predict(X)
print(cluster.labels_)

from scipy.cluster.hierarchy import dendrogram, linkage


linked = linkage(X, 'single')

labelList = range(1, 11)

plt.figure(figsize=(10, 7))
dendrogram(linked,
            orientation='top',
            labels=labelList,
            distance_sort='descending',
            show_leaf_counts=True)
plt.show()'''
from scipy.spatial import distance
X = [(0.0,0.0),
     (0.5,0.0),
     (0.0,2.0),
     (2.0,2.0),
     (2.5,8.0),
     (6.0,3.0),
     (7.0,3.0)]
print('\n \n PROXIMITY MATRIX : ')
print( distance.cdist(X, X, 'cityblock'))
from scipy.cluster.hierarchy import dendrogram, linkage


linked = linkage(X, 'average',metric ='cityblock')

labelList = range(1, 8)

plt.figure(figsize=(10, 7))
dendrogram(linked,
            orientation='top',
            labels=labelList,
            distance_sort='descending',
            show_leaf_counts=True)
plt.show()









