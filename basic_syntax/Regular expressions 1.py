import numpy as np

url ='https://en.wikipedia.org/w/index.php?title=List_of_rodents&action=raw'

mice = np.loadtxt(url, dtype=str, delimiter='\t', skiprows=1)

print(mice)

for species in mice:
    if species in [r"\*\*\s*''\[\[(\w+)\s(\w+)\]\]''"]:
        print(species)


import requests
import re

# Step 1: Download the wiki markup content
url = 'https://en.wikipedia.org/w/index.php?title=List_of_rodents&action=raw'
data = requests.get(url)

# Step 2: Parse the content to find Latin binomials using regular expressions
# Regular expression to find species in the format **''[[Genus species]]''
species_pattern = re.compile(r"\*\*\s*''\[\[(\w+)\s(\w+)\]\]''")

# Find all matches
species_list = species_pattern.findall(data.text)
# Step 3: Export the list to a text file with genus and species separated by a comma
output_file = 'species_list.txt'

with open(output_file, 'w') as file:
    for genus, species in species_list:
        file.write(f"{genus},{species}\n")

print(f"Species list has been saved to {output_file}")
