#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 17:56:02 2019

@author: root
"""

from scipy.spatial import distance
X = [(0.0,0.0),
     (0.5,0.0),
     (0.0,2.0),
     (2.0,2.0),
     (2.5,8.0),
     (6.0,3.0),
     (7.0,3.0)]

Y = [(2.5,8),
     (0.625,1),
     (6.5,3)]
y = distance.cdist(X, Y, 'euclidean')
print(y)


