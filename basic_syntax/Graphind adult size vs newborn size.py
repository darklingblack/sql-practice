import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_path = r'C:\Users\barba\OneDrive - University College London\Bioinformatics\BIoPythonTraining\Programming for Biologists\Mammal_lifehistories_v2.txt'

dataset = pd.read_csv(file_path, delimiter='\t', skipfooter=7, na_values=['-999', '-999.00']) # or just 
df = pd.DataFrame(dataset)

print(df)

ad_mass = df['mass(g)']
new_mass = df['newborn(g)']
plt.figure(figsize=(10, 5))
plt.plot(ad_mass)
plt.plot(new_mass)
plt.show()

log_ad_mass = np.log10(ad_mass)
log_new_mass = np.log10(new_mass)
plt.plot(log_ad_mass)
plt.plot(log_new_mass)
plt.show()

rodentia_df = df[df['order'] == 'Rodentia']
log_ad_mass_rodentia = np.log10(rodentia_df['mass(g)'].dropna())
log_new_mass_rodentia = np.log10(rodentia_df['newborn(g)'].dropna())
plt.plot(log_ad_mass_rodentia)
plt.plot(log_new_mass_rodentia)
plt.show()
------------------------------------------------------------------------------

plt.figure(figsize=(8, 6))
plt.scatter(log_ad_mass_rodentia, log_new_mass_rodentia, c='blue', label='Rodentia')
plt.xlabel('Log10 of Adult Mass (g)')
plt.ylabel('Log10 of Newborn Mass (g)')
plt.title('Log10 of Adult Mass vs. Log10 of Newborn Mass for Rodentia')
plt.legend()
plt.grid(True)
plt.show()