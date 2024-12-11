import pandas as pd
import numpy as np
import csv

file_path = 'MOMv3.3.txt'
columns = ["continent", "status", "order", "family", "genus", "species", "log_mass", "mass", "reference"]
data = pd.read_csv(file_path, delimiter='\t', names=columns, header=None)

# Exclude species designated as "historical" in the 'status' column
# Not needed but kept to remember

data = data[data['mass'] > 0]

data = data[data['status'] != 'historical']

# Combine genus and species to create the latin binomial
data['latin_binomial'] = data['genus'] + ' ' + data['species']

# Get unique species count
unique_species = np.unique(data['latin_binomial'])
num_unique_species = unique_species.size #when you need the total number of elements in the DataFrame.

# Count extinct and extant species
num_extinct = data[data['status'] == 'extinct'].shape[0] # when you need to know the structure of the DataFrame, specifically the number of rows and columns.
num_extant = data[data['status'] == 'extant'].shape[0] # it gives back the order

# .shape[0] was used to count the number of rows (species) that matched a certain condition (e.g., extinct or extant species).
# .size would not be appropriate for counting rows because it would return the total number of elements, not just the number of rows.

# Get unique genera count
unique_genera = np.unique(data['genus'])
num_unique_genera = unique_genera.size

# Find the largest and smallest species by mass
largest_species = data.loc[data['mass'].idxmax()]
smallest_species = data.loc[data['mass'].idxmin()]

# Calculate the average mass of extinct and extant species
mean_mass_extinct = data[data['status'] == 'extinct']['mass'].mean()
mean_mass_extant = data[data['status'] == 'extant']['mass'].mean()

print(f"The average mass of extant species is {mean_mass_extant:.2f} grams and the average mass of extinct species is {mean_mass_extant:.2f}.")

############################################################################################################

def export_to_csv(data, filename):
    """Export list of lists to comma delimited text file"""
    outputfile = open(filename, 'w', newline='')
    datawriter = csv.writer(outputfile)
    datawriter.writerows(data)

# Prepare the results list
results = [["continent", "avg_mass_extant", "avg_mass_extinct", "mass_difference"]]

# Ensure 'continent' column contains only strings
data['continent'] = data['continent'].astype(str)

# Calculate the mean masses for extant and extinct species by continent
# Get unique continents
continents = np.unique(data['continent'])
for continent in continents:
    continent_data = data[data['continent'] == continent]
    avg_mass_extant = continent_data[continent_data['status'] == 'extant']['mass'].mean()
    avg_mass_extinct = continent_data[continent_data['status'] == 'extinct']['mass'].mean()
    mass_difference = avg_mass_extant - avg_mass_extinct
    results.append([continent, avg_mass_extant, avg_mass_extinct, mass_difference])
    export_to_csv(results, r'C:\Users\barba\OneDrive - University College London\Bioinformatics\BIoPythonTraining\Programming for Biologists\continent_mass_differences.csv')
