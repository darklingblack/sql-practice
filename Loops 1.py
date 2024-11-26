import numpy as np

url = 'https://raw.githubusercontent.com/ethanwhite/progbio/master/data/dna_sequences_1.txt'

data = np.loadtxt(url, dtype=str)

def get_gc_content(data):
        gc_perc = []
        gc_calc = ((data.count('c') + data.count('g')) / len(data)) * 100
        gc_perc.append(gc_calc)
        return gc_perc

tot_gc = [get_gc_content(data) for data in data]

for row in tot_gc:
    print(row)