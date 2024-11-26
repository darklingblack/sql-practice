import numpy as np
import pandas as pd #just to double check the data

url = "https://raw.githubusercontent.com/ethanwhite/progbio/gh-pages/data/shrub_volume_experiment.csv"

numpy_data = np.loadtxt(url, delimiter=',', skiprows=1, dtype=float)

data = pd.read_csv(url) #just to double check the data
numpy_array = data.to_numpy()
print(numpy_array) #same thing as numpy_data
print(numpy_data)
print(data)

for i in range(numpy_data.shape[0]):
    sample = numpy_data[i, :]
    print(sample) #same thing as numpy_data

for i in range(numpy_data.shape[0]):
    width = numpy_data[i, 3]
    print(width)

for i in range(numpy_data.shape[0]):
    experiment = numpy_data[i, 1]
    print(experiment)    

for i, sample in enumerate(numpy_data):
    heigth_mes = 'tall' if heigth > 5 else 'medium' if 2 <= heigth < 5 else 'short'

total_carbon = []

def calculate_total_carbon(heigth, width, length):
    volume = heigth * width * length
    total_carbon = 1.8 + 2 * np.log(volume)
    return total_carbon

total_carbon_values = []

for i, sample in enumerate(numpy_data):
    site = numpy_data[i, 0]
    experiment = numpy_data[i, 1]
    length = numpy_data[i, 2]
    width = numpy_data[i, 3]
    heigth = numpy_data[i, 4]
    total_carbon = calculate_total_carbon(heigth, width, length)
    total_carbon_values.append(total_carbon)
    #first print
    print(f"Total Carbon = {total_carbon}")
    #second print
    print(f"Sample {i+1}: Total Carbon = {total_carbon}") 
    #third print
    print(total_carbon_values)

table = []

for i, sample in enumerate(numpy_data):
    site = numpy_data[i, 0]
    experiment = numpy_data[i, 1]
    length = numpy_data[i, 2]
    width = numpy_data[i, 3]
    heigth = numpy_data[i, 4]
    total_carbon = calculate_total_carbon(heigth, width, length)
    total_carbon_values.append(total_carbon)
    heigth_mes = 'tall' if heigth > 5 else 'medium' if 2 <= heigth < 5 else 'short'
    table.append((experiment, heigth_mes, total_carbon))
    #fifth print
    print("Experiment | Height Category | Shrub Carbon")
    for row in table:
        print(f"{row[0]} | {row[1]} | {row[2]:.4f}")

import csv

def export_to_csv(table, filename):
	with open(filename, 'w', newline='') as outputfile:
	    datawriter = csv.writer(outputfile)
	    datawriter.writerows(table)
	    outputfile.close()

filename = []
filename = r'C:\Users\barba\OneDrive - University College London\Bioinformatics\BIoPytonTraining\Programming for Biologists\shrubs_experiment_results4.csv'

export_to_csv(table, filename)

print(f"CSV file exported successfully to: C:\\Users\\barba\\OneDrive - University College London\\Bioinformatics\\BIoPytonTraining\\Programming for Biologists\\shrubs_experiment_results.csv")

    