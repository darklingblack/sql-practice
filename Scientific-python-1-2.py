import pandas as pd

file_path = r'C:\Users\barba\OneDrive - University College London\Bioinformatics\BIoPythonTraining\Programming for Biologists\MOMv3.3.txt' # Load and inspect the dataset
df = pd.read_csv(file_path, delimiter='\t')
print(df.columns)
print(df.head())
print(df.iloc[1])

filtered_mass = df[df['Data2'] > 0] # Filter DataFrame for non-negative mass and relevant statuses
print(filtered_mass.loc[filtered_mass['Data2'].idxmin()])
print(filtered_mass.loc[filtered_mass['Data2'].idxmax()])

relevant_mass = filtered_mass[filtered_mass['Status'].isin(['extinct', 'extant'])] # Further filter for 'extinct' and 'extant'

print(f"The average mass of extant species is {relevant_mass[relevant_mass['Status'] == 'extant']['Data2'].mean():.2f} and the average mass of extinct species is {relevant_mass[relevant_mass['Status'] == 'extinct']['Data2'].mean():.2f}.")

grouped_mass = relevant_mass.groupby(['Loc', 'Status'])['Data2'].mean().unstack() # Group by 'Loc' and calculate means
grouped_mass['Difference'] = grouped_mass['extant'] - grouped_mass['extinct']
grouped_mass = grouped_mass.reset_index()

columns_order = ['Loc', 'extant', 'extinct', 'Difference'] # Define columns order and export to CSV
grouped_mass = grouped_mass[columns_order]
output_path = r'C:\Users\barba\OneDrive - University College London\Bioinformatics\BIoPythonTraining\Programming for Biologists\output_filename.csv'
grouped_mass.to_csv(output_path, index=False)
print("Data exported successfully to", output_path)
