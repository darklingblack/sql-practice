
import numpy as np #

url = 'https://raw.githubusercontent.com/ethanwhite/progbio/master/data/dna_sequences_1.txt'

seq = np.loadtxt(url, dtype=str)

def get_gc_content(seq):
    gc_contents = []
    for sequence in seq:
        gc_count = sequence.count('c') + sequence.count('g')
        gc_percent = (gc_count / len(sequence)) * 100
        gc_contents.append(gc_percent)
    return gc_contents

tot_gc = get_gc_content(seq) 

for i in tot_gc:
    print(i)




#To calculate the GC content for each sequence in the NumPy array, you'll need to iterate over each sequence and apply the GC content calculation to each individual sequence string. Here's how you can modify your code to achieve this
