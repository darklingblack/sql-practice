w = 10.2
x = 1.3
y = 2.8
z = 17.5
dna1 = 'attattaggaccaca'
dna2 = 'attattaggaacaca'
species1 = 'diplodocus'
species2 = 'tyrannosaurus'

#1
w > 10
#2
w + x < 15
#3
x > y
#4
2 * x > y
#5
dna1 == dna2
#6
dna1 != dna2
#7
dna1.count('t') == dna2.count('t')
#8
product = x * w
13.2 < product < 13.5
#9
species2 < species1
#10
w > x and y > z
#11
len(dna1) < 5 or z < w*x 
#12
len(dna1) + len(dna2) >= 30
#13
import numpy
(w + x + y) / numpy.log10(100) == 7.15
#14
(((dna1.count('c') + dna1.count('g')) / len(dna1)) * 100) == (((dna2.count('c') + dna2.count('g')) / len(dna2)) * 100)
