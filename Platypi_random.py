import random

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

    def successful_seasons(self):
        return sum(1 for eggs in self.eggs_laid if eggs > 0)

    def __str__(self):
        return f"Platypus(name={self.name}, eggs_laid={self.eggs_laid})"

# Create three Platypus objects
platypi = [
    Platypus("perry", []),
    Platypus("quacker", []),
    Platypus("fishface", [])
]

# Simulate 10 seasons of egg laying
for _ in range(10):
    for platypus in platypi:
        eggs = random.randint(0, 3)
        platypus.add_season_eggs(eggs)

# Print out the results
for platypus in platypi:
    print(f"{platypus.name} laid a total of {platypus.total_eggs()} eggs in {platypus.successful_seasons()} successful breeding seasons.")


####################################################################################
# If I had 10 different seasons:

platypi = [
    Platypus("perry", [3, 2, 4, 1, 2, 0, 1, 3, 2, 4]),
    Platypus("quacker", [1, 0, 3, 2, 2, 1, 0, 3, 2, 1]),
    Platypus("fishface", [0, 1, 2, 3, 1, 2, 1, 0, 3, 2])
]

for platypus in platypi:
    print(f"{platypus.name} laid a total of {platypus.total_eggs()} eggs in {platypus.successful_seasons()} successful breeding seasons.")

####################################################################################
# What if I had three season and had to generate 7 more?

platypi = [
    Platypus("perry", [3, 2, 4]),
    Platypus("quacker", [1, 0, 3]),
    Platypus("fishface", [0, 1, 2])
]

# Generate egg counts for the remaining 7 seasons
for platypus in platypi:
    for _ in range(7):
        eggs = random.randint(0, 3)
        platypus.add_season_eggs(eggs)

# Print out the results
for platypus in platypi:
    print(f"{platypus.name} laid a total of {platypus.total_eggs()} eggs in {platypus.successful_seasons()} successful breeding seasons.")