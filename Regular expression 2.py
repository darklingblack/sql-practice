import requests
import re
import sqlite3

# Step 1: Download the wiki markup content
url = 'https://en.wikipedia.org/w/index.php?title=List_of_rodents&action=raw'
data = requests.get(url)

# Step 2: Define regular expressions for family and species
family_pattern = re.compile(r"==\s*Family\s+(\w+)==")
species_pattern = re.compile(r"\*\*\s*''\[\[(\w+)\s(\w+)\]\]''")

# Step 3: Initialize variables
species_list = []
current_family = ""

# Step 4: Parse the content line by line
for line in data.text.splitlines():
    # Try to match a family in the current line
    family_match = family_pattern.search(line) #As you parse each line, you need to check if a new family starts, so you can update the current_family context.
    
    # If a family is found, update the current_family
    if family_match:
        current_family = family_match.group(1) #Group 0: This is always the entire match.
                                                #Group 1: This is the first capturing group, which in this case is (\w+)
    
    # Try to match a species in the current line
    species_match = species_pattern.search(line)
    
    # If a species is found and we have a current family
    if species_match and current_family:
        genus, species = species_match.groups()
        species_list.append((current_family, genus, species))

conn = sqlite3.connect('rodents.db')
cursor = conn.cursor()

# Step 6: Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS rodents (
    id INTEGER PRIMARY KEY,
    family TEXT,
    genus TEXT,
    species TEXT
)
''')

# Step 7: Insert data into the table
for family, genus, species in species_list:
    cursor.execute('INSERT INTO rodents (family, genus, species) VALUES (?, ?, ?)', (family, genus, species))

# Step 8: Commit and close the connection
conn.commit()
conn.close()

print(f"Species data has been saved to the SQLite database 'rodents.db'")


# Step 5: Export the list to a text file with family, genus, and species separated by commas
output_file = 'all_list.txt'

with open(output_file, 'w') as file:
    for family, genus, species in species_list:
        file.write(f"{family},{genus},{species}\n")

print(f"Species list has been saved to {output_file}")

import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('rodents.db')
cursor = conn.cursor()

# Execute a query
cursor.execute('SELECT * FROM rodents')
rows = cursor.fetchall()

# Print the results
for row in rows:
    print(row)

# Close the connection
conn.close()
