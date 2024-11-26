# Tests_1_file.py

import urllib.request
import csv
import pandas as pd
from io import StringIO

def get_gc_content(dnaseq):
    dnaseq = dnaseq.replace("\n", "").replace("\r", "").upper()
    gc_count = dnaseq.count('G') + dnaseq.count('C')
    return (100 * gc_count / len(dnaseq)) if len(dnaseq) > 0 else 0

def get_size_class(earlength):
    if earlength is None:
        return 'invalid'
    try:
        earlength = float(earlength)
    except ValueError:
        return "invalid"
    
    if earlength >= 15:
        return 'extralarge'
    elif 10 <= earlength < 15:
        return 'large'
    elif 8 <= earlength < 10:
        return 'medium'
    elif earlength < 8:
        return 'small'
    return 'invalid'

def get_data_from_web(url, datatype, headerrow=False):
    with urllib.request.urlopen(url) as webpage:
        datareader = csv.reader(webpage.read().decode('utf-8').splitlines())
        if headerrow:
            next(datareader)  # skip the header row
        data = [row for row in datareader]
    return data

def export_to_csv(data, filename):
    with open(filename, 'w', newline='') as output_file:
        datawriter = csv.writer(output_file)
        datawriter.writerows(data)

def process_data(data):
    results = []
    for _, row in data.iterrows():
        id = row['id']
        earlength = row['earlength']
        dnaseq = row['dnaseq']
        gc_count = get_gc_content(dnaseq)
        earlength_category = get_size_class(float(earlength))
        results.append((id, earlength_category, gc_count))
    results_df = pd.DataFrame(results, columns=['id', 'earlength_category', 'gc_content'])
    return results_df

def calculate_gc_content_by_size_class(results_df):
    avg_gc_content = results_df.groupby('earlength_category')['gc_content'].mean().reset_index()
    return avg_gc_content

def main_process(url, output_file):
    data = get_data_from_web(url)
    results_df = process_data(data)
    avg_gc_content_df = calculate_gc_content_by_size_class(results_df)
    export_to_csv(avg_gc_content_df, output_file)
    return avg_gc_content_df

if __name__ == '__main__':
    url = 'https://raw.githubusercontent.com/ethanwhite/progbio/6fedcc4968646ece437e4ed28dd2a1e190d6f7b2/data/houseelf_earlength_dna_data.csv'
    output_file = '3grangers_output_avg.csv'
    avg_gc_content_df = main_process(url, output_file)
    print(avg_gc_content_df)