sequences = ['ttgaatgccttacaactgatcattacacaggcggcatgaagcaaaaatatactgtgaaccaatgcaggcg',
             'gauuauuccccacaaagggagugggauuaggagcugcaucauuuacaagagcagaauguuucaaaugcau',
             'gaaagcaagaaaaggcaggcgaggaagggaagaagggggggaaacc',
             'guuuccuacaguauuugaugagaaugagaguuuacuccuggaagauaauauuagaauguuuacaacugcaccugaucagguggauaaggaagaugaagacu',
             'gauaaggaagaugaagacuuucaggaaucuaauaaaaugcacuccaugaauggauucauguaugggaaucagccggguc']

def dna_or_rna(sequence):
    if 'u' in sequence and 't' in sequence:
        return 'UNKNOWN'
    elif 'u' in sequence:
        return 'RNA'
    elif 't' in sequence:
        return 'DNA'
    else:
        return 'UNKNOWN'

for i in sequences:
    print(dna_or_rna(i))

list = []

def dna_or_rna_multivalue(list_of_sequences):
    for i in list_of_sequences:
        result = dna_or_rna(i)
        list.append(result)
    return list

list_of_sequences = ['attgcccaat', 'agcuucua', 'attuuccaga',
'ggcccacacgg', 'atattagcc', 'startcodon', 'uucaaggu', 'tttttttttt',
'aaaaaaaaa']

list = dna_or_rna_multivalue(list_of_sequences)
for j in list:
    print(j)