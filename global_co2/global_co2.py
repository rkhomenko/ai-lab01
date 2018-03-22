#!/usr/bin/env python3

import matplotlib.pyplot as plt, numpy as np
from pandas import read_csv
from sklearn import linear_model
from itertools import combinations

header = [
    'Gas Fuel',
    'Liquid Fuel',
    'Solid Fuel',
    'Cement',
    'Gas Flaring',
    'Per Capita'
]

data = None
with open('global_co2.csv') as csv_file:
    data = read_csv(csv_file)

nan = float('Nan')

data_null = data.copy()
data_max = data.copy()

data_null['Per Capita'] = data_null['Per Capita'].replace(nan, 0)

data_max['Per Capita'] = data_max['Per Capita'].replace(nan, 1.5)

def generate_combo_figs(data, suffix):
    for combo in combinations(header, 2):
        plt.xlabel(combo[0])
        plt.ylabel(combo[1])
    
        x = data[combo[0]].as_matrix()
        y = data[combo[1]].as_matrix()

        file_name = '{}-{}-{}.svg'.format(combo[0], combo[1], suffix).replace(' ', '_')

        plt.plot(x, y, 'ro')
        plt.savefig(file_name)
        plt.clf()

generate_combo_figs(data_null, 'null')
generate_combo_figs(data_max, 'max')
