import numpy as np

url = "https://raw.githubusercontent.com/ethanwhite/progbio/gh-pages/data/gainesville_precip.csv"

numpy_data = np.loadtxt(url, delimiter=',')

import matplotlib.pyplot as plt

print(numpy_data[1])

import statistics

sample = []

def average_rain(numpy_data):
    num_columns = numpy_data.shape[1] #this indicates that columns will be interested, not their values yet
    print(num_columns)
    column_averages = []
    for col in range(num_columns):
        column_data = numpy_data[:, col]  # Access column data
        column_average = np.mean(column_data)  # Calculate column average
        column_averages.append(column_average)
    return column_averages

averages = average_rain(numpy_data)
print(averages)

plt.plot(averages)
plt.show()