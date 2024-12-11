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

newlist = []
newlist = [n.name for n in platypi if any(p > 3 for p in n.eggs_laid)]
print(newlist)

print(platypi.name) 
platypi.breeding_season(5) 
print(platypi.total_eggs())
platypi.add_season_eggs(3) 
print(platypi.total_eggs()) 
print(platypi)               

#############################################################################################

perry = Platypus("Perry", [5, 3, 2])
print(perry.total_eggs())  # Output: 10
perry.breeding_season(4)
print(perry.eggs_laid)  # Output: [5, 3, 2, 4]
print(perry)  # Output: Platypus(name=Perry, eggs_laid=[5, 3, 2, 4])

########################################################################################

class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says Woof!")

my_dog = Dog("Fido")
my_dog.bark()  # Output: Fido says Woof!


