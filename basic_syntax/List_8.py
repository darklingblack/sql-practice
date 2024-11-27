sequences = ['GCCATTCTGC', 'GCTTACCCAA', 'CCTCTAGCGC', 'TAAATTTTGT',
'TGTGATACTG', 'AACAGAGCATCTCTTGTGACCAGTT', 'TAGGCTGCCTGTGGCAGGTTGTTGCATTCTCTTAGAACCGCCCTGAACTC', 'ATCCACAGACATCTCGTGTAAGGGG', 'CCCTCTTTCCAATTGACAGGATCAG']

from Bio.Seq import Seq

dna_compl = []

for i in sequences:
    compl  = Seq(i) #Seq(i) converts each sequence string into a Seq object so that you can use the methods provided by the Bio.Seq module.
    dna_compl.append(compl.complement())

for i in dna_compl:
    print(i)