import urllib.request
import csv

def get_gc_content(dnaseq):
    gc_content = (100 * dnaseq.count('G') + dnaseq.count('C')) / len(dnaseq)
    return gc_content

def get_size_class(earlength):
    if earlength > 15:
        size_class = 'extralarge'
    elif earlength > 10:
        size_class = 'large'
    elif earlength > 8:
        size_class = 'medium'
    else:
        size_class = 'small'
    return size_class

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

if __name__ == '__main__':
    elves_data = get_data_from_web('https://raw.githubusercontent.com/ethanwhite/progbio/6fedcc4968646ece437e4ed28dd2a1e190d6f7b2/data/houseelf_earlength_dna_data.csv', 'csv', headerrow=True)

results = []
for row in elves_data:
    id, earlength, dnaseq = row
    gc_content = get_gc_content(dnaseq)
    earlength_category = get_size_class(float(earlength))  # Convert earlength to float before categorization
    results.append((id, earlength_category, gc_content))

size_groups = {}
for id, size_class, gc_content in results:
    if size_class not in size_groups:
        size_groups[size_class] = []
        size_groups[size_class].append(gc_content)

avg_results = []
for size_class, gc_values in size_groups.items():
    avg_gc_content = sum(gc_values) / len(gc_values)
    avg_results.append([size_class, avg_gc_content])

export_to_csv(results, 'grangers_output.csv')