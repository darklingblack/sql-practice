mkdir assignment_directory

svn add assignment_directory
svn add Shell_2-2.py
svn add assignment_directory/sar_areas.csv
svn add assignment_directory/sar_model_data.csv

svn move sar_areas.csv assignment_directory/
svn move sar_model_data.csv assignment_directory/

svn commit -m "Added assignment_directory and related files"
svn commit -m "Moved area and model data files to assignment_directory"

svn update

svn commit -m "Added assignment_directory and related files"
svn commit -m "Moved area and model data files to assignment_directory"

mkdir assignment_directory/new_folder1
mkdir assignment_directory/new_folder2
svn add assignment_directory/new_folder1
svn add assignment_directory/new_folder2

svn commit -m "Added new_folder1 and new_folder2 to assignment_directory"

nano predict_richness.sh

# 3. Add the following content to predict_richness.sh
#!/bin/bash

# Combine all area files into one
cat sar_areas* > combined_areas.txt

# Run the combined file through the Python script
python Shell_2-2.py combined_areas.txt predicted_diversities.txt

# The -k option specifies the key (or column) to sort by.
# 1,1 indicates that the sort should be performed using the first column only. 
# The syntax 1,1 means to start and end the sort key on the first column.
# Post-process the output file to ensure uniqueness and sorting
sort -n -k1,1 predicted_diversities.txt | uniq > sorted_predicted_diversities.txt

# Move the final output to the expected file name
mv sorted_predicted_diversities.txt predicted_diversities.txt

######################################################

# 4. Make the shell script executable
chmod +x predict_richness.sh

./predict_richness.sh

# Run the shell script
bash predict_richness.sh

# Add the new files to SVN:
svn add predict_richness.sh predicted_diversities.txt

# Commit the changes:
svn commit -m "Added predict_richness.sh and predicted_diversities.txt"

# Optional Step: Modify and Commit rich_pred.py
# If you choose to modify rich_pred.py to make it a self-contained unit:
# Edit rich_pred.py:
nano rich_pred.py

# Modify the script to include the necessary functions and use fileinput.input(). For example:
import fileinput

# python
def predict_richness(area):
    # Replace this with the actual function for predicting richness
    return float(area) * 1.23  # Example calculation

if __name__ == "__main__":
    for line in fileinput.input():
        area = line.strip()
        richness = predict_richness(area)
        print(f"{area}\t{richness}")

# sh
svn commit -m "Updated rich_pred.py with self-contained code"

# Move Files to modeldata Directory
# If you need to create a modeldata directory and move areas.txt files into it, do the following:
mkdir modeldata
svn move sar_areas.csv modeldata/
svn move sar_model_data.csv modeldata/

#!/bin/bash


# Navigate to the assignment directory
cd "$(dirname "$0")"

# Find all areas files in subdirectories and combine them into one file
find modeldata -name 'sar_areas*.csv' -exec cat {} + > combined_areas.txt

# Run the combined file through the Python script
python Shell_2-2.py combined_areas.txt predicted_diversities.txt

# Post-process the output file to ensure uniqueness and sorting
sort -n -k1,1 predicted_diversities.txt | uniq > sorted_predicted_diversities.txt

# Move the final output to the expected file name
mv sorted_predicted_diversities.txt predicted_diversities.txt

#############################################################################
chmod +x predict_richness.sh

bash predict_richness.sh

# Move the file to the working directory first

mv Shell_2-2.py "C:\Users\barba\OneDrive - University College London\Bioinformatics\BIoPythonTraining\Programming for Biologists\SVNwc\assignment_directory"

# Or this 

mv Shell_2-2.py "SVNwc/assignment_directory"

cd "C:\Users\barba\OneDrive - University College London\Bioinformatics\BIoPythonTraining\Programming for Biologists\SVNwc\assignment_directory"

########################################################################################
#!/bin/bash

# Navigate to the assignment directory
cd "$(dirname "$0")"

output_file="combined_areas.txt"
cat modeldata/sar_areas*.csv > "$output_file"
# Find all areas files in subdirectories and combine them into one file

# Run the combined file through the Python script
python Shell_2-2.py "$output_file" predicted_diversities.txt

# Post-process the output file to ensure uniqueness and sorting
sort -n -k1,1 predicted_diversities.txt | uniq > sorted_predicted_diversities.txt

# Move the final output to the expected file name
mv sorted_predicted_diversities.txt predicted_diversities.txt


# the svn status output shows that both Higher_order_functions_2-2.py and assignment_directory are currently not under version control (indicated by the ?).
# First, you need to add both the file and the directory to SVN.
dir


svn revert --recursive assignment_directory
svn revert -R .
svn cleanup

svn move sar_areas.csv assignment_directory/
svn move sar_model_data.csv assignment_directory/

svn commit -m "Random message" # This is to conclude the previous command. The message must be included but it is random