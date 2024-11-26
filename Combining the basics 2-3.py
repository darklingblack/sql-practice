import numpy as np

url = "https://raw.githubusercontent.com/ethanwhite/progbio/gh-pages/data/shrub_volume_experiment.csv"

# Load data using numpy.loadtxt, skipping the header row
data = np.loadtxt(url, delimiter=',', skiprows=1, dtype=float)

# Define a function to calculate total carbon
def calculate_total_carbon(heigth, width, length):
    volume = heigth * width * length
    total_carbon = 1.8 + 2 * np.log(volume)
    return total_carbon


table = []

# Process each row of data
for row in data:
    experiment_number = int(row[0])
    heigth = row[4]
    width = row[3]
    length = row[2]
    if heigth > 5:
        heigth_category = 'tall'
    elif 2 <= heigth < 5:
        heigth_category = 'medium'
    else:
        heigth_category = 'short'

    # Calculate shrub carbon
volume = heigth * width * length
shrub_carbon = calculate_total_carbon(heigth, width, length)

    # Append row to table
table.append([experiment_number, heigth_category, shrub_carbon])

# Iterate over each sample in the table and print all attributes
for sample in table:
    experiment_number, heigth_category, shrub_carbon = sample
    print(f"Experiment Number: {experiment_number}")
    print(f"Heigth Category: {heigth_category}")
    print(f"Shrub Carbon: {shrub_carbon:.4f}")
    print()  # Print a blank line for separation

# Print the entire table
for row in table:
    print(row)
