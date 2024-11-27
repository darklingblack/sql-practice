def get_mass_from_length_theropoda(length):
    tot_mass = []
    for l in length:
        mass = 10.95 * (l ** 2.64)
        tot_mass.append(mass)
    return tot_mass

length = [10.1, 9.5, 11.2, 9.8, 10.4, 12.0, 11.5, 9.5, 9.8, 10.0, 10.7, 10.2, 11.9, 9.7, 11.2, 11.8, 10.7]

tot_thero = get_mass_from_length_theropoda(length)
for i in tot_thero:
        print(i)