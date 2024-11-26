import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = r'C:\Users\barba\OneDrive - University College London\Bioinformatics\BIoPythonTraining\Programming for Biologists\MOMv3.3.txt'

dataset = pd.read_csv(file_path, delimiter='\t') # or just 
df = pd.DataFrame(dataset)
print(df.columns)
print(df.head())
print(df.iloc[1])

df.groupby(['Genus', 'Species']).size()

filtered_mass = df[df['Data2'] > 0] #Data2 = Mass

min_data2_row = filtered_mass.loc[filtered_mass['Data2'].idxmin()]  # Row with smallest 'Data2'
max_data2_row = filtered_mass.loc[filtered_mass['Data2'].idxmax()]

print(min_data2_row)
print(max_data2_row)

filtered_status = filtered_mass[filtered_mass['Status'].isin(['extinct', 'extant'])] # Filter DataFrame to include only extinct and extant species

avg_mass_extinct = filtered_status[filtered_status['Status'] == 'extinct']['Data2'].mean() # Calculate average mass for extinct and extant species
avg_mass_extant = filtered_status[filtered_status['Status'] == 'extant']['Data2'].mean()
print(f"The average mass of extant species is {avg_mass_extant:.2f} and the average mass of extinct species is {avg_mass_extinct:.2f}.")

cont_mass = filtered_status.groupby(['Loc', 'Status'])['Data2'].mean().unstack()
cont_mass['Difference'] = cont_mass['extant'] - cont_mass['extinct']

final_df = cont_mass.reset_index()

print(final_df)

output_path = r'C:\Users\barba\OneDrive - University College London\Bioinformatics\BIoPythonTraining\Programming for Biologists\continent_mass_differences.csv'
final_df.to_csv(output_path, index=False)

final_df['log_avg_extinct'] = np.log10(final_df['extinct'] + 1) #got avg in cont_mass
final_df['log_avg_extant'] = np.log10(final_df['extant'] + 1) #got avg in cont_mass

print(final_df)

locations = final_df['Loc'].unique()
for loc in locations: # Loop over each location
    data_loc = final_df[final_df['Loc'] == loc] # Filter data for the current location
    plt.figure(figsize=(10, 5)) # Plot histograms # Adjust the figure size as needed
    plt.hist(data_loc['log_avg_extinct'].dropna(), bins=20, alpha=0.5, label='log_avg_extinct')
    plt.hist(data_loc['log_avg_extant'].dropna(), bins=20, alpha=0.5, label='log_avg_extant')
    plt.title(f'Histograms for Location {loc}')
    plt.xlabel('Log Values')
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()
    # Show or save the plot
    plt.savefig(f'Histogram_{loc}.png') 
---------------------------------------------------------------------------------------------

continents = filtered_status['Loc'].unique()
for continent in continents:
    cont_log_extinct = log_avg_extinct[('Loc')]
    cont_log_extant = log_avg_extant[('Loc')]
    plot_histograms(cont_log_extinct, cont_log_extant, continent)

plt.hist(log_avg_extinct)
plt.hist(log_avg_extant)
plt.show()
---------------------------------------------------------------------------------------------------------------------------

# Rename 'Loc' to 'Continent'
final_df = final_df.rename(columns={'Loc': 'Continent'})
columns_order = ['Continent', 'extant', 'extinct', 'Difference']
final_df = final_df[columns_order]

avg_cont_extinct = avg_mass_extinct[avg_mass_extinct['Status'] == 'extinct'].groupby('Loc')
avg_cont_extant = filtered_status[filtered_status['Status'] == 'extant'].groupby('Loc')['Data2'].mean().reset_index()

diff_cont_avg = avg_cont_extinct avg_cont_extant

avg_cont_extinct = avg_mass_extinct.groupby('Loc')['Data2']

avg_cont_extinct = filtered_status[filtered_status['Status'] == 'extinct']['Data2'].mean() # Calculate average mass for extinct and extant species

continent_mass = filtered_mass.groupby('Loc')['Data2'].mean()

filtered_loc = filtered_mass[filtered_mass['Loc'].iterrows()]

-------------------------------------------------------------------------------

print(df[df['Status'].isin(['extinct', 'extant'])])

extinct_species_df = df[df['Status'] == 'extinct']
print("Extinct Species:") # Print information about the extinct species
for index, row in extinct_species_df.iterrows():
    genus = row['Genus']
    species = row['Species'] # You can include additional columns here if needed
    print(f"Genus: {genus}, Species: {species}") # Print the information about each extinct species

extant_species_df = df[df['Status'] == 'extant']
print("Extant Species:") # Print information about the extant species
for index, row in extant_species_df.iterrows():
    genus = row['Genus']
    species = row['Species']  # You can include additional columns here if needed
    print(f"Genus: {genus}, Species: {species}")    # Print the information about each extant species


extinct_species_df = df[df['Status'] == 'extinct']
extant_species_df = df[df['Status'] == 'extant']

df.groupby(['Genus']).size()
len(df.groupby(['Genus', 'Species']))
len(df.groupby(['Genus']))
len(df.groupby(['Species']))

min_data2 = filtered_df['Data2'].min()

largest_species = filtered_df.loc[filtered_df['Data2'].idxmax()] # Find the row with the largest mass (maximum value) - We use idxmax() and idxmin() to get the index of the row with the largest and smallest mass values, respectively, from filtered_df.

smallest_species = filtered_df.loc[filtered_df['Data2'].idxmin()] # Find the row with the smallest mass (minimum value) - We then use .loc[] to retrieve the entire row corresponding to these indices, representing the largest and smallest species.
min_mass = df[df['Data2'] > 0]['Data2'].min()
max_mass = df[df['Data2'] > 0]['Data2'].max()

df.groupby(['Status']).size()
df.groupby(['Family']).size()


