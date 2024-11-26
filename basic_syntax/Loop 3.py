import numpy as np

url = 'https://raw.githubusercontent.com/ethanwhite/progbio/master/data/shrub_dimensions.csv'

headers = ['ShrubID', 'Length', 'Width', 'Heigth']

data = np.loadtxt(url, delimiter=',')

print(data)

volumes =[]

for row in data:
    length, width, heigth = row
    volume = length * width * heigth
    volumes.append(volume)

for index, volume in enumerate(volumes):
    print(f"The volume of the shrub {index} is: {volume:.2f}.")