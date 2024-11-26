import math
import numpy as np
# Given area

area = 10
side_length = math.sqrt(area)
side_length_rounded = round(side_length, 2)
print(f"The length of one side of the square is {side_length_rounded} meters.")

number_of_species = 3.5 + (0.25 * np.log(8))

print(round(number_of_species, 2))

