import pandas as pd
import numpy as np
import sys
from scipy.special import logsumexp

# Load parameter data from a local CSV file
df_par = pd.read_csv('sar_model_data.csv', header=None, names=['ID', 'b0', 'b1', 'b2'])
df_par['b2'] = df_par['b2'].fillna('NaN')
print(df_par)

# Read area data from the file specified in the command line argument
input_file = sys.argv[1]
df_area = pd.read_csv(input_file, header=None, names=['Area'])
print(df_area)

# Define model functions
def power(area, b0, b1, b2=None):
    return float(b0) * (area ** float(b1))

def power_quadratic(area, b0, b1, b2):
    return 10 ** (float(b0) + float(b1) * np.log10(area) + float(b2) * (np.log10(area) ** 2))

def logarithmic(area, b0, b1, b2=None):
    return float(b0) + float(b1) * np.log(area)

def michaelis_menten(area, b0, b1, b2=None):
    return float(b0) * area / (float(b1) + area)

def lomolino(area, b0, b1, b2):
    try:
        log10_area = np.log10(area)
        exponent = (log10_area ** (float(b2) / area))
        stable_exponent = float(b1) ** exponent
        return float(b0) / (1 + stable_exponent)
    except OverflowError:
        return float('inf')  # Or some other appropriate value
    except (ValueError, ZeroDivisionError):
        return float('nan')  # Return NaN for invalid operations

# Model function mapping
models = {
    'Power': power,
    'PowerQuadratic': power_quadratic,
    'Logarithmic': logarithmic,
    'MichaelisMenten': michaelis_menten,
    'Lomolino': lomolino
}

# Calculate predictions
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
    print(f"Area: {area}, Mean Richness: {mean_richness}")

# Convert results to DataFrame and remove duplicates
results_df = pd.DataFrame(results, columns=['Area', 'Mean Predicted Richness']).drop_duplicates()

# Sort the DataFrame by Area
results_df = results_df.sort_values(by='Area')

# Save the sorted, unique results to the output file specified in the command line argument
output_file = sys.argv[2]
results_df.to_csv(output_file, index=False, sep='\t')
print(f"Results written to {output_file}")
