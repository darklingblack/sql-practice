class Platypus:
    def __init__(self, name, eggs_laid):
        self.name = name
        self.eggs_laid = eggs_laid

    def total_eggs(self):
        return sum(self.eggs_laid)

    def breeding_season(self, eggs):
        self.eggs_laid.append(eggs)

    def add_season_eggs(self, eggs):
        self.eggs_laid.append(eggs)

    def __str__(self):
        return f"Platypus(name={self.name}, eggs_laid={self.eggs_laid})"

platypi = [Platypus("perry", [3,2,4,1,2]),
Platypus("quacker", [100,1,3,1,2]),
Platypus("fishface", [0,1,3,1,2,1]),
Platypus("duckhead", [3,1,3,6,3]),
Platypus("waddles", [3,1,2,0,8,3]),
Platypus("professor quackington", [2,1,4,5,7]),
Platypus("bartholomew beavertail", [0,1,3,1,0,0,2]),
Platypus("syd", [3,1,3,1,3,5,5,2,1,3]),
Platypus("ovide", [2,0,10,0,0,0,0,0,0]),
Platypus("hexley", [3,1,2,3,1,0,0,1,1]),
Platypus("supafly", [19,1,2,1,0,0,0,1])]

print(platypi)

# Example usage

print(platypi.name)          # Output: "perry"
platypi.breeding_season(5)   # Adds 5 to the eggs_laid list
print(platypi.total_eggs())  # Output: 17
platypi.add_season_eggs(3)   # Adds 3 to the eggs_laid list
print(platypi.total_eggs())  # Output: 20
print(platypi)               # Output: Platypus(name=perry, eggs_laid=[3, 2, 4, 1, 2, 5, 3])

#############################################################################################
'
Platypus Class
==================== The provided code defines a Platypus class in Python.

' Initialization 
' The __init__ method is a special method that is automatically called when an object of the class is created. It initializes the attributes of the class.

' In this case, the __init__ method takes two parameters: name and eggs_laid. name is a string representing the name of the platypus, and eggs_laid is a list of integers representing the number of eggs laid by the platypus in each breeding season.

' Methods '
total_eggs()
# The total_eggs method returns the total number of eggs laid by the platypus across all breeding seasons. It does this by summing up all the values in the eggs_laid list.

breeding_season(eggs)
# The breeding_season method allows you to add the number of eggs laid by the platypus in a new breeding season. It takes an integer eggs as a parameter and appends it to the eggs_laid list.

add_season_eggs(eggs)
# The add_season_eggs method is identical to the breeding_season method. It also allows you to add the number of eggs laid by the platypus in a new breeding season.

str()
#  The __str__ method is a special method that returns a string representation of the object. In this case, it returns a string in the format Platypus(name=<name>, eggs_laid=<eggs_laid>), where <name> is the name of the platypus and <eggs_laid> is the list of eggs laid.

# Example Usage
# Here's an example of how you could use this class:

perry = Platypus("Perry", [5, 3, 2])
print(perry.total_eggs())  # Output: 10
perry.breeding_season(4)
print(perry.eggs_laid)  # Output: [5, 3, 2, 4]
print(perry)  # Output: Platypus(name=Perry, eggs_laid=[5, 3, 2, 4])

########################################################################################

# what is the self parameter?

# The self parameter

# In Python, self is a conventionally used parameter name in class methods that refers to the instance of the class.

# When a method is called on an instance of a class, Python automatically passes the instance as the first argument to the method. By convention, this first argument is named self.

# The self parameter is used to access variables and methods that belongs to the class. It's a way to refer to the current object being manipulated.

# Here's an example:


class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says Woof!")

my_dog = Dog("Fido")
my_dog.bark()  # Output: Fido says Woof!

# In the above example, when we call my_dog.bark(), Python automatically passes my_dog as the first argument to the bark method. Inside the bark method, self refers to my_dog, so self.name refers to my_dog.name, which is "Fido".

# By using self, we can access and manipulate the attributes and methods of the class instance.

# Note that self is not a keyword in Python, it's just a conventionally used name. You could use any other name, but it's strongly recommended to use self for readability and consistency.



