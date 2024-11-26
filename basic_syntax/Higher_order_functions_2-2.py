import pandas as pd
import numpy as np

# URLs of the CSV files
url_par = 'https://raw.githubusercontent.com/ethanwhite/progbio/master/data/sar_model_data.csv'
url_area = 'https://raw.githubusercontent.com/ethanwhite/progbio/master/data/sar_areas.csv'

# Fetch the parameters CSV file content using pd.read_csv
df_par = pd.read_csv(url_par, header=None, names=['ID', 'b0', 'b1', 'b2'])

# Fill missing b2 values with NaN
df_par['b2'] = df_par['b2'].fillna(np.nan)

# Fetch the areas CSV file content using pd.read_csv
df_area = pd.read_csv(url_area, header=None, names=['Area'])

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
            if b2 != 'NaN':  # Only add b2 if it's not NaN
                params.append(float(b2))
            richness.append(model_func(*params))
    mean_richness = np.mean(richness)
    results.append([area, mean_richness])

# Create a new dataframe to store the results
results = pd.DataFrame(results, columns=['Area', 'Mean Predicted Richness'])

# Convert results to DataFrame and save to CSV
results.to_csv(r"C:\Users\barba\OneDrive - University College London\Bioinformatics\BIoPythonTraining\Programming for Biologists\SVNwc\assignment_directory\predicted_richness.csv", index=False)