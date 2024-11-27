class Platypus:
    def __init__(self, name, eggs_laid): # The __init__ method in Python is a special method called a constructor. It is automatically called when a new instance (object) of a class is created. 
        self.name = name                # This method is typically used to initialize the instance's attributes (variables) and to set up any initial state for the object.
        self.eggs_laid = eggs_laid      # The __init__ method is defined with the first parameter self, which refers to the instance being created.
    
    def lay_eggs(self, num_eggs):
        self.eggs_laid.append(num_eggs)
    
    def total_fecundity(self):
        return sum(self.eggs_laid)
    
    def __repr__(self):
        return f"Platypus(name='{self.name}', eggs_laid={self.eggs_laid})"

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
    