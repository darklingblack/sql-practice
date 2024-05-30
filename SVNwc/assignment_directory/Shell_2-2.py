#!/usr/bin/env python

import pandas as pd
import numpy as np
import fileinput
import io

file_path = 'modeldata/sar_areas.csv'  # Adjust the file path as needed

# Collect all lines from the file
lines = []
with fileinput.input(files=file_path) as file:
    for line in file:
        lines.append(line)

# Join the lines into a single string
file_content = ''.join(lines)

# Use io.StringIO to convert the string to a file-like object
file_like = io.StringIO(file_content)

# Read the CSV data
df_area = pd.read_csv(file_like, header=None, names=['Area'])
# URLs of the CSV files
url_par = 'https://raw.githubusercontent.com/ethanwhite/progbio/master/data/sar_model_data.csv'

# Fetch the parameters CSV file content using pd.read_csv
df_par = pd.read_csv(url_par, header=None, names=['ID', 'b0', 'b1', 'b2'])

# Fill missing b2 values with NaN
df_par['b2'] = df_par['b2'].fillna(np.nan)

# Print the DataFrames to verify
print(df_par)
print(df_area)

def power(area, b0, b1, b2=None):
    return b0 * area ** b1

def power_quadratic(area, b0, b1, b2):
    return 10 ** (b0 + b1 * np.log10(area) + b2 * (np.log10(area) ** 2))

def logarithmic(area, b0, b1, b2=None):
    return b0 + b1 * np.log(area)

def michaelis_menten(area, b0, b1, b2=None):
    return b0 * area / (b1 + area)

def lomolino(area, b0, b1, b2):
    return b0 / (1 + b1 ** (np.log10(area) ** (b2 / area)))

models = {
    'Power': power,
    'PowerQuadratic': power_quadratic,
    'Logarithmic': logarithmic,
    'MichaelisMenten': michaelis_menten,
    'Lomolino': lomolino
}

results = []
for area in df_area['Area']:
    richness = []
    for model_name, (b0, b1, b2) in zip(df_par['ID'], zip(df_par['b0'], df_par['b1'], df_par['b2'])):
        if model_name in models:
            model_func = models[model_name]
            params = [area, float(b0), float(b1)]
            if not pd.isna(b2):  # Only add b2 if it's not NaN
                params.append(float(b2))
            richness.append(model_func(*params))
    mean_richness = np.mean(richness)
    results.append([area, mean_richness])

# Create a new dataframe to store the results
results = pd.DataFrame(results, columns=['Area', 'Mean Predicted Richness'])

# Save results to CSV
results.to_csv('predicted_richness.csv', index=False)
