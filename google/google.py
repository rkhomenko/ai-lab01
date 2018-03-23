#!/usr/bin/env python3

import matplotlib.pyplot as plt, numpy as np
from pandas import read_csv
from sklearn import linear_model
from itertools import combinations

data = None
with open('google.csv') as csv_file:
    data = read_csv(csv_file)

print(data.corr())

header = [
    'Open', 
    'High',
    'Low',
    'Adj. Open',
    'Adj. High', 
    'Adj. Low', 
    'Adj. Close',
]

def fit(data):
    x = data[header].as_matrix()
    y = data['Close'].as_matrix()

    reg = linear_model.LinearRegression()
    reg.fit(x, y)
        
    n = len(reg.coef_)
    for i in range(0, n):
        plt.xlabel(header[i])
        plt.ylabel('Close')
        plt.plot(data[header[i]].as_matrix(), y, 'ro')

        t = np.arange(data[header[i]].min(), data[header[i]].max(), 0.1)
        plt.plot(t, reg.coef_[i] * t + reg.intercept_)

        plt.savefig('Close-{}.svg'.format(header[i]).replace(' ', '-'))
        plt.clf()

fit(data)
