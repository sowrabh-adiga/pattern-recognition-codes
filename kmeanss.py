#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 18:44:40 2019

@author: root
"""

from sklearn.cluster import KMeans
import numpy as np

X = np.array([[0.0,0.0],
              [0.5,0.0],
              [0.0,2.0],
              [2.0,2.0],
              [2.5,8.0],
              [6.0,3.0],
              [7.0,3.0]])
kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
print(kmeans.labels_)
print(kmeans.predict([[0, 0], [7, 3]]))
print(kmeans.cluster_centers_)

