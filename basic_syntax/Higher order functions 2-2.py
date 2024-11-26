import pandas as pd
import numpy as np
import requests
from io import StringIO

# URLs of the CSV files
url_par = 'https://raw.githubusercontent.com/ethanwhite/progbio/master/data/sar_model_data.csv'
url_area = 'https://raw.githubusercontent.com/ethanwhite/progbio/master/data/sar_areas.csv'

# Fetch the parameters CSV file content using requests
response_par = requests.get(url_par)
data_par = response_par.text

response_area = requests.get(url_area)
data_area = response_area.text

df_par = pd.read_csv(StringIO(data_par), header=None, names=['ID', 'b0', 'b1', 'b2'])

# Fill missing b2 values with NaN
df_par['b2'] = df_par['b2'].fillna('NaN')

# Print the DataFrame to verify
print(df_par)

df_area = pd.read_csv(StringIO(data_area), header=None, names=['Area'])

# Print the DataFrame to verify
print(df_area)

def power(area, b0, b1, b2=None):
    return float(b0) * (area ** float(b1))

def power_quadratic(area, b0, b1, b2):
    return 10 ** (float(b0) + float(b1) * np.log10(area) + float(b2) * (np.log10(area) ** 2))

def logarithmic(area, b0, b1, b2=None):
    return float(b0) + float(b1) * np.log(area)

def michaelis_menten(area, b0, b1, b2=None):
    return float(b0) * area / (float(b1) + area)

def lomolino(area, b0, b1, b2):
    return float(b0) / (1 + float(b1) ** (np.log(area) ** (float(b2) / area)))

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

# Convert results to DataFrame and save to CSV
results_df = pd.DataFrame(results, columns=['Area', 'Mean Predicted Richness'])
results_df.to_csv('predicted_richness.csv', index=False)