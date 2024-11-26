def apply_to_each(func, iterable):
    return [func(x) for x in iterable]

def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]
squared_numbers = apply_to_each(square, numbers)
print(squared_numbers)

-----------------------------------------------------------------------------------------

#use it on a different terminal to check the efficacy

#map takes a function and an iterable as arguments and returns a new iterable that is the result of applying the function to each element in the original iterable:

def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))
print(squared_numbers)

-----------------------------------------------------------------------------------

#filter takes a function and an iterable as arguments and returns a new iterable that contains only the elements from the original iterable for which the function returns True

def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(is_even, numbers))
print(even_numbers)

-----------------------------------------------------------------------------------------

#reduce takes a function and an iterable as arguments and returns a single value that is the result of reducing the iterable to a single value using the function. For example:

from functools import reduce

def add(x, y):
    return x + y

numbers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(add, numbers)
print(sum_of_numbers)

----------------------------------------------------------------------------------------

#If n is 0, the factorial of 0 is defined as 1. This is the base case for the recursion.
#The expression if n else 1 ensures that when n is 0, the function returns 1.

def factorial(n):
    return n * factorial(n-1) if n else 1

factorial(10)      # no previously cached result, makes 11 recursive calls

factorial(5)       # just looks up cached value result

factorial(12)      # makes two new recursive calls, the other 10 are cached

factorial(0)       # returns 1

-------------------------------------------------------------------------------------
#The __init__ method is a special method in Python classes, known as the initializer or constructor. It is automatically called when a new instance of the class is created. Its purpose is to initialize the instance's attributes.

import statistics

def __init__(self, sequence_of_numbers):
    self._data = tuple(sequence_of_numbers)

def stdev(self):
    return statistics.stdev(self._data)

-----------------------------------------------------------------------------

# The __name__ variable is a built-in variable in Python that represents the name of the module in which it is used. When a Python script is run, Python sets the __name__ variable to '__main__'. If the script is being imported into another module, __name__ will be set to the name of the script/module.

def main():
    print("This script is being run directly.")

def another_function():
    print("This function is part of the module.")

if __name__ == "__main__":
    main()

-------------------------------------------------------------------------------
import urllib.request

def get_pep(num):
    resource = f'https://peps.python.org/pep-{num:04d}'
    try:
        with urllib.request.urlopen(resource) as s:
            return s.read()
    except urllib.error.HTTPError:
        return 'Not Found'

for n in 8, 290, 308, 320, 8, 218, 320, 279, 289, 320, 9991:
    n_values = []
    pep = get_pep(n)
    print(n, len(pep))
    n_values.append(n)