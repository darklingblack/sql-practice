def get_mass_from_length_theropoda(length):
    tot_mass = []
    mass = 0.73 * length ** 3.63
    tot_mass.append(mass)
    return mass
  
length = 16

tot_thero = get_mass_from_length_theropoda(length)

print(tot_thero)



def get_mass_from_length(length2):
    tot_mass2 = []
    mass2 = 214.44 * length2 ** 1.46
    tot_mass2.append(mass2)
    return mass2

length2 = 26

tot_thero2 = get_mass_from_length(length2)

print(tot_thero2)