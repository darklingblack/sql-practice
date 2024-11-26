conversion_factors = {
    'J': 1,
    'KJ': 1000,
    'CAL': 4.1868,
    'KCAL': 4186.8
}

def convert_energy_units_to_joule(energy_value, input_unit, output_unit):
    if input_unit not in conversion_factors:
        print("Sorry, I don't know how to convert from " + input_unit)
        return None
    if output_unit not in conversion_factors:
        print("Sorry, I don't know how to convert to " + output_unit)
        return None
    result_in_joule = energy_value * conversion_factors[input_unit]
    conversion = result_in_joule / conversion_factors[output_unit]
    return conversion

energy_in_cals = 200
energy_in_joules = convert_energy_units_to_joule(energy_in_cals, 'CAL', 'J')
print(f"{energy_in_cals} CAL is {energy_in_joules} J")

daily_energy_kcal = 2500
daily_energy_joules = convert_energy_units_to_joule(daily_energy_kcal, 'KCAL', 'J')
print(f"2500 KCAL is {daily_energy_joules} J")

seal_energy_kj = 52500  # KJ/day
seal_energy_joules = convert_energy_units_to_joule(seal_energy_kj, 'KJ', 'J')
human_energy_joules = daily_energy_joules
times_more_energy = seal_energy_joules / human_energy_joules
print(f"A common seal uses {times_more_energy:.2f} times more energy than a human.")

erg_conversion = convert_energy_units_to_joule(1, 'KCAL', 'ERG')

# Instead of writing an individual conversion between each of the different currencies (which would require 12 if statements) you could choose to convert all of the input units to a 
# common scale and then convert from that common scale to the output units. This approach is especially useful since we might need to add new units later and this will be much easier using this approach.