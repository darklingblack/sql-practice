sequences = ['GCTTACCCAA', 'gctaatta', 'CCTCTAGCGC', 'TAAATTTTGT', 'TGTGATACTG',
             'AACAGAGCATCTCTTGTGACCAGTT', 'TAGGCTGCCTGTGGCAGGTTGTTGCATTCTCTTAGAACCGCCCTGAACTC', 'ATCCACAGACATCTCGTGTAAGGGG',
             'CCCTCTTTCCAATTGACAGGATCAG', 'taggattgacctagaaa']

sequences[-1] = sequences[-1].upper()
sequences[1] = sequences[1].upper()


print(sequences)
#Print the list to the screen. Remember, the GC content is just the
#number of G's plus the number of C's divided by the total number of
#bases.

#You may use a function if you wish, but it is not necessary.

#Write a program that uses a for loop to produce a list of the GC contents of the following sequences (copy this list into your code):

gc_content = []

for seq in sequences:
    gc = (seq.count('G') + seq.count('C'))/(len(seq))
    gc_content.append(gc)

for seq, gc in zip(sequences, gc_content):
    print(f"GC content of {seq}: {gc:.2%}")

#Issue: Instead of appending the result to the gc_content list, this line gc_content = (seq.count('G') + seq.count('C')) / len(seq) reassigns the gc_content variable to the calculated GC content (a float). This means gc_content is no longer a list after the first iteration, but a single float value.

#esult: The list gc_content is replaced by a single float value during the first iteration of the loop, and thus the variable gc_content is not iterable in the subsequent code.