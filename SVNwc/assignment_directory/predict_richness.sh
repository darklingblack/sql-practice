#!/bin/bash

# Set the output file
output_file="combined_areas.txt"

# Combine all sar_areas.csv files in subdirectories into one file
find modeldata -type f -name "sar_areas.csv" -exec cat {} + > "$output_file"

# Make the Python script executable
chmod +x Shell_2-2.py

# Run the combined file through script.py
./Shell_2-2.py "$output_file"

# Clean up the combined file
rm "$output_file"

# Post-process the output file to ensure uniqueness and sorting
sort -n -k1,1 predicted_richness.csv | uniq > sorted_predicted_richness.csv

# Move the final output to the expected file name
mv sorted_predicted_richness.csv predicted_richness.csv
