class Platypus:
    def __init__(self, name, eggs_laid): # The __init__ method in Python is a special method called a constructor. It is automatically called when a new instance (object) of a class is created. 
        self.name = name                # This method is typically used to initialize the instance's attributes (variables) and to set up any initial state for the object.
        self.eggs_laid = eggs_laid      # The __init__ method is defined with the first parameter self, which refers to the instance being created.
    
    def lay_eggs(self, num_eggs):
        self.eggs_laid.append(num_eggs)
    
    def total_fecundity(self):
        return sum(self.eggs_laid)

class BetterPlatypus(Platypus):
    def __init__(self, name, eggs_laid, unhatched_eggs):
        super().__init__(name, eggs_laid)
        self.unhatched_eggs = unhatched_eggs
    
    def lay_eggs(self, hatched, unhatched):
        self.eggs_laid.append(hatched)
        self.unhatched_eggs.append(unhatched)
    
    def total_fecundity(self):
        return sum(self.eggs_laid) + sum(self.unhatched_eggs)

# Example usage
perry = BetterPlatypus("perry", [3, 2, 4, 1, 2], [0, 1, 0, 0, 1])
print(perry.total_fecundity()) 
perry.lay_eggs(2, 1)
print(perry.total_fecundity()) 
