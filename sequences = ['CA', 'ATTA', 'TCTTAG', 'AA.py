sequences = ['CA', 'ATTA', 'TCTTAG', 'AAGA', 'CG', 'CGAGC']
repeats = [10, 2, 5, 7, 20, 6]

def rep_seq(sequences, repeats):
    tot_seqs = [] #to create an empty list that will be used permanently
    for i, j in zip(sequences, repeats): #i is sequences and j is repeats
        tot_seq = i * j #this is temporary
        tot_seqs.append(tot_seq) #this holds permanently
    return tot_seqs

seq_len = rep_seq(sequences, repeats) #this holds the algorithm of the functionfo

for seq in seq_len: #seq could be anything because is in for - in
    print(seq)

FROM THE PROPER RESULT

def generate_full_sequences(sequences, repeats):
    full_sequences = []
    for seq, count in zip(sequences, repeats):
        full_sequence = seq * count
        full_sequences.append(full_sequence)
    return full_sequences

result = generate_full_sequences(sequences, repeats)

for sequence in result:
    print(sequence) 
