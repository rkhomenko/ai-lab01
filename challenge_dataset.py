#!/usr/bin/env python3

import matplotlib.pyplot as plt, numpy as np
from sklearn import linear_model
from pandas import read_csv

csv_file = open('challenge_dataset.txt')

data = read_csv(csv_file)
x = data['x'].as_matrix()
y = data['y'].as_matrix()

plt.xlabel('x')
plt.ylabel('y')
plt.plot(x, y, 'ro')

reg = linear_model.LinearRegression()
reg.fit(x.reshape(-1, 1), y)

t = np.arange(4.5, 25, 0.1)
plt.plot(t, reg.coef_[0] * t + reg.intercept_)
plt.savefig('challenge_dataset.svg')
