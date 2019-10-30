#!/usr/bin/env python2
import numpy as np
import pandas as pd

matrix = pd.read_csv('p081_matrix.txt', header=None).values

#matrix = [131, 673, 234, 103, 18,
#        201, 96, 342, 965, 150,
#        630, 803, 746, 422, 111,
#        537, 699, 497, 121, 956, 
#        805, 732, 524, 37, 331]
#matrix = np.reshape(matrix, (5,5))
#
#print matrix, matrix.shape

dim = matrix.shape[0]
summed_matrix = np.zeros(matrix.shape)
for i in xrange(dim-1, -1, -1):
    for j in xrange(dim-1, -1, -1):
        if i==j and i==dim-1:
            summed_matrix[i,j] = matrix[i,j]
            continue
        try:
            right=summed_matrix[i, j+1]
        except:
            right=np.inf
        try:
            down=summed_matrix[i+1, j]
        except:
            down=np.inf
        
        summed_matrix[i,j] = matrix[i,j] + min(right, down)
#        print i, j, matrix[i,j], right, down

print summed_matrix[0,0]
