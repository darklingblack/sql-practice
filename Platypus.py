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

# Example usage
perry = Platypus("perry", [3, 2, 4, 1, 2])
print(perry.name)          # Output: "perry"
perry.breeding_season(5)   # Adds 5 to the eggs_laid list
print(perry.total_eggs())  # Output: 17
perry.add_season_eggs(3)   # Adds 3 to the eggs_laid list
print(perry.total_eggs())  # Output: 20
print(perry)               # Output: Platypus(name=perry, eggs_laid=[3, 2, 4, 1, 2, 5, 3])

