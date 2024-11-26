a = 'ctgccctgcccctggagggtggccccaccggccgagacag'

b = 'ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCCCCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCCTCCTGACTTTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGAAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGCAATCCGCGCGCCGGGACAGAATGCCCTGCAGGAACTTCTTCTGGAAGACCTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAGTTTAATTACAGACCTGAA'

c = 'ccctgcccctggagggtctgccctgcccctggagggtctgccctgcccctggagggtctgccctgcccctggagggtctgccctgcccctggagggttgc'

d = 'CTGCAGGAACTTCTTCTGGAAGACCTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAG'

def get_gc_content(a, b, c, d):
    gc_perc = []
    for seq in a, b, c, d:
        if 'c' in seq and 'g' in seq:
            gc_calc = ((seq.count('c') + seq.count('g')) / len(seq)) * 100
        if 'C' in seq and 'G' in seq:
            GC_CALC = ((seq.count('C') + seq.count('G')) / len(seq)) * 100
            gc_perc.append(GC_CALC)
            gc_perc.append(gc_calc)
    return gc_perc

def get_gc_content(a, b, c, d):
    gc_perc = []
    for seq in [a, b, c, d]:
        seq_lower = seq.lower() # Normalize sequence to lowercase: everything lowercase
        gc_calc = ((seq_lower.count('c') + seq_lower.count('g')) / len(seq)) * 100
        gc_perc.append(gc_calc)
    return gc_perc

gc_perc = get_gc_content(a, b, c, d)

if len(a) < 100 or len(b) < 100 or len(c) < 100 or len(d) < 100:
    print("Warning in: One or more sequences are less than 100 base pairs long and therefore the calculated GC content may not accurately reflect that of the broader region of the genome.")

sequence_names = ['a', 'b', 'c', 'd']
sequences = [a, b, c, d]

for name, seq in zip(sequence_names, sequences):
    if len(seq) < 100:
        print(f"Warning: Sequence {name} is less than 100 base pairs long and therefore the calculated GC content may not accurately reflect that of the broader region of the genome.")

for i in gc_perc:
    print(i)

for name, j in zip(sequence_names, gc_perc):
    print(f"GC content of sequence {name}: {j:.2f}%")