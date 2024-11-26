def get_mass_from_length_theropoda(length):
    tot_mass = []
    mass = 0.73 * length ** 3.63
    tot_mass.append(mass)
    return mass

length = 16

tot_thero = get_mass_from_length_theropoda(length)

tot_thero_p = 2.2046 * tot_thero

print(tot_thero_p)