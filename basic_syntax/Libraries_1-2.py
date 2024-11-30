import main_script_equation as mse

areas = [1, 5.2, 10.95, 152.3, 597.6, 820, 989.8, 1232.5, 15061]
custom_params = {
        'Power': [20.81, 0.1896, None],  # Example parameters, adjust as needed
        'PowerQuadratic': [1.35, 0.1524, 0.0081],
        'Logarithmic': [14.36, 21.16, None],
        'MichaelisMenten': [85.91, 42.57, None],
        'Lomolino': [1082.45, 1.59, 390000000]
}

# Call the function to estimate species richness
results = mse.estimate_species_richness(areas, custom_params)

# Print the results
for result in results:
    print(f"Area: {result[0]}, Estimated Richness: {result[1]}")

mse.power(15, 7, 9)

power = mse.power

power(15, 7, 9)

# In script_equations there are the algorithm for each custom parameter
# In main_script_equation there is the code to how calculate each area for each parameter in each custom
# At the end it is just possible to change the area value and have the result immediatly
