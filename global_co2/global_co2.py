#!/usr/bin/env python3

import matplotlib.pyplot as plt, numpy as np
from pandas import read_csv
from sklearn import linear_model
from itertools import combinations

data = None
with open('global_co2.csv') as csv_file:
    data = read_csv(csv_file)

nan = float('Nan')
average = data['Per Capita'].mean()

data_null = data.copy()
data_max = data.copy()
data_average = data.copy()

data_null['Per Capita'] = data_null['Per Capita'].replace(nan, 0)
data_max['Per Capita'] = data_max['Per Capita'].replace(nan, 1.5)
data_average['Per Capita'] = data_average['Per Capita'].replace(nan, average)

print("************ null corr ***************")
print(data_null.corr())
print("************ max corr ***************")
print(data_max.corr())
print("************ average corr ***************")
print(data_average.corr())

header = [
    'Gas Fuel',
    'Liquid Fuel',
    'Solid Fuel',
    'Cement',
    'Per Capita'
]

def fit(data, suffix):
    x = data[header].as_matrix()
    y = data['Gas Flaring'].as_matrix()

    reg = linear_model.LinearRegression()
    reg.fit(x, y)
        
    n = len(reg.coef_)
    for i in range(0, n):
        plt.xlabel(header[i])
        plt.ylabel('Gas Flaring')
        plt.plot(data[header[i]].as_matrix(), y, 'ro')

        t = np.arange(data[header[i]].min(), data[header[i]].max(), 0.1)
        plt.plot(t, reg.coef_[i] * t + reg.intercept_)

        plt.savefig('Gas_Flaring-{}-{}.svg'.format(header[i], suffix).replace(' ', '-'))
        plt.clf()

fit(data_null, 'null')
fit(data_max, 'max')
fit(data_average, 'average')
