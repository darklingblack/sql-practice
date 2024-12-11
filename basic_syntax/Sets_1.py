import pandas as pd
import numpy as np
from itertools import combinations

file_path = 'TGPP_pres.csv'

output_file = 'jaccard.csv'

data = pd.read_csv(file_path)

df = pd.DataFrame(data)

df = df.dropna(subset=['plot', 'year', 'spcode'])

print(df.head())#

unique_plot = np.unique(df['plot'])
num_unique_plot = unique_plot.size

# The apply(set) method in the context of a pandas DataFrame or Series is used to apply the Python set constructor to each element in the Series. 
# This is particularly useful when you want to transform lists or collections of items within each group into sets.
speceS_by_year_output = 'speces_by_year_output.csv'

species_by_site_year = df.groupby(['plot', 'year'])['spcode'].apply(set).reset_index()

species_by_site_year.to_csv(speceS_by_year_output, index=False)

# We are only interested in whether or not the species occurs within the plot.
# J = C / (S(A) + S(B) - C) 

def jaccard_similarity(set1, set2):
    intersection_size = len(set1.intersection(set2)) 
    union_size = len(set1) + len(set2) - len(set1.intersection(set2))
    if union_size == 0:
        return 1.0  # If both sets are empty, define their similarity as 1
    return intersection_size / union_size  # Jaccard similarity J = C / (S(A) + S(B) - C)

all_similarities = []
# This is to compare plos within the same year
for (i, site1), (j, site2) in combinations(species_by_site_year.iterrows(), 2):
    if site1['year'] == site2['year']: # Ensure that we only compare plots within the same year
        plot1, plot2 = site1['plot'], site2['plot']
        set1, set2 = site1['spcode'], site2['spcode']
        similarity = jaccard_similarity(set1, set2)
        all_similarities.append((site1['year'], plot1, plot2, similarity))

similarities_df = pd.DataFrame(all_similarities, columns=['year', 'plot1', 'plot2', 'jaccard_similarity'])

similarities_df.to_csv(output_file, index=False)

print(f"Jaccard similarities have been saved to {output_file}")

Jaccard = len(set1.intersection(set2)) / (len(set1) + len(set2) - len(set1.intersection(set2)))

# This is to compare the same plot across different years:
# if site1['plot'] == site2['plot']:
#     year1, year2 = site1['year'], site2['year']

S(A) = len(plot); S(B) = len(plot)

site1_species.union(site2_species)  # or set1 | set2

site2_species.union(site1_species)

site1_species.intersection(site2_species)  # or set1 & set2

site2_species.intersection(site1_species)  # or set1 & set2

site1_species.difference(site2_species)  # or set1 - set2

site2_species.difference(site1_species)  # or set1 - set2

site1_species.symmetric_difference(site2_species)  # or set1 ^ set2

site2_species.symmetric_difference(site1_species)  # or set1 ^ set2

site1_species = {"lion", "tiger", "bear"}
site2_species = {"tiger", "bear", "wolf"}
