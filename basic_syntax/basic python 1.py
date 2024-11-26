data = [['A1', 28], ['A2', 32], ['A3', 1], ['A4', 0],
        ['A5', 10], ['A6', 22], ['A7', 30], ['A8', 19],
		['B1', 145], ['B2', 27], ['B3', 36], ['B4', 25],
		['B5', 9], ['B6', 38], ['B7', 21], ['B8', 12],
		['C1', 122], ['C2', 87], ['C3', 36], ['C4', 3],
		['D1', 0], ['D2', 5], ['D3', 55], ['D4', 62],
		['D5', 98], ['D6', 32]]

print("The total number of sites is", len(data))

print("The total number of birds at the 7th site is", data[6][1])

print("The total number of birds at the last site is", data[25][1])

def total_birds(data):
    return sum(sample[1] for sample in data)

print("The total number of birds is", total_birds(data))

import statistics

def average_birds(data):
    return statistics.mean(sample[1] for sample in data)

print("The average number of birds seen on a site is", average_birds(data))

def total_birds_C(data):
    return sum(sample[1] for sample in data if sample[0].startswith('C'))

print("The total number of birds beginning with C is", total_birds_C(data))
