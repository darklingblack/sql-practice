import csv
import math
import pandas as pd
import numpy as np

#### NOT USEFUL, COULD USE ONLY pd.read_csv()

def load_data(file_path):
    data =[]
    with open(file_path, 'r') as output_file:
        for line in output_file:
            row = line.strip().split('\t')
            data.append(row)
        return data

file_path = r'C:\Users\barba\OneDrive - University College London\Bioinformatics\BIoPythonTraining\Programming for Biologists\Macroplot_data_Rev.txt'

all_dataset = load_data(file_path)

#### It was possible to use only "pd.read_csv()" to retrieve everything

#or df = pd.DataFrame(file_path)
data2 = pd.read_csv(file_path, delimiter='\t')

print(data2.columns)

def circumferences_to_diameters(circumferences):
    return circumferences / math.pi

def diameters_to_biomass(diameters):
    return 0.124 * diameters ** 2.53

# vars = variables
# var = variable

melted_data = data2.melt(id_vars=["PlotID", "SpCode"], 
                        value_vars=["TreeGirth1", "TreeGirth2", "TreeGirth3", "TreeGirth4", "TreeGirth5"], 
                        var_name="TreeGirthType", 
                        value_name="Girth")

# Filter out zero values (no measurement)
filtered_data = melted_data[melted_data['Girth'] > 0]

# Convert circumferences to diameters
filtered_data.loc[:, 'Diameter'] = circumferences_to_diameters(filtered_data['Girth'])
#without .loc it worked for both
# Calculate biomass
filtered_data.loc[:, 'Biomass'] = diameters_to_biomass(filtered_data['Diameter'])

# Calculate the total biomass
total_biomass = filtered_data['Biomass'].sum()

print(f"Total biomass: {total_biomass:.2f} kg")
