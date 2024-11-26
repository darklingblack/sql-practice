import csv
import math

filename = (r'C:\Users\barba\Downloads\TGPP_cover.csv.')

def load_data(filename):
    data = []
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
        return data
    
csv_data = load_data(filename)

def euclidean_distance(data):
    for row in csv_reader:
        if row['cover'] in ['1', '2']:
        sqrt(sum((N1_i - [3] ==(2)_i)^2))
