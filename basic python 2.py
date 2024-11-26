import pandas as pd
def get_data_from_web(url):
        data = pd.read_csv(url)
        return data

url = "https://raw.githubusercontent.com/ethanwhite/progbio/6fedcc4968646ece437e4ed28dd2a1e190d6f7b2/data/houseelf_earlength_dna_data.csv"

loaded_data = get_data_from_web(url)

df = pd.read_csv(url)

for index, row in df.iterrows(): #it has been addded for refresh, from 12 to 18 is useless
    ear_length = row['earlength']
    dna_sequence = row['dnaseq']
    id_n = row['id']
    print(row['earlength'])
    print(row['dnaseq'])
    print(row['id'])

for index, row in df.iterrows():
   ear_size = 'large' if row['earlength'] > 10 else 'small'

df['ear_size'] = df['earlength'].apply(lambda x: 'large' if x > 10 else 'small')

gc_content = dnaseq.count('C') + dnaseq.count('G') / len(dnaseq) * 100

def gc_count(dnaseq):
    return (dnaseq.count('C') + dnaseq.count('G')) / len(dnaseq) * 100

df['gc_content'] = df['dnaseq'].apply(gc_count)

print(df['gc_content'])

new_df = df[["ear_size", "gc_content"]].copy()

new_df[['gc_content']].to_csv(r'C:\Users\barba\OneDrive - University College London\Bioinformatics\BIoPytonTraining\Programming for Biologists\grangers_analysis2.csv.')
