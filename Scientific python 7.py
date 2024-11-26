import pandas as pd
import csv
import numpy as np

url = 'https://raw.githubusercontent.com/ethanwhite/progbio/master/data/shrub_volume_experiment.csv'

data = pd.read_csv(url, delimiter=',')

df = pd.DataFrame(data)

print(data.iloc[0]) # only the first row
print(data.iloc[:, 0]) # all rows but only first and second columns
print(data.iloc[:, [0, 2]]) # all rows but only first and second columns

print(data[['site']])
print(data[['site', 'length']])

print(data[['length']])

shrub_carbon = (df['length'] * df['width'] * df['height'])
print(shrub_carbon)

all_shrub = 1.8 + 2 * np.log(shrub_carbon)
print(all_shrub)

big_heights = df[df['height'] > 5]['height']
print(big_heights)

data_means = df.groupby('site').mean() # After this line, data_means is a DataFrame that looks like this (for example):
data_means['height']

#           length    width   height
# experiment                              
# 1           2.500000  2.575000  4.700000
# 2           2.700000  2.650000  5.100000
# 3           2.566667  2.100000  4.100000

data_means = df.groupby('experiment').mean()
data_means['height']

data_high = df.groupby('site').max()
data_high['height']
