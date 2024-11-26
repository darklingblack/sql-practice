import sys
import numpy as np
import script_equations as eq  # replace 'yourname' with your actual name

# Dictionary of models imported from yourname_equations module
models = {
    'Power': eq.power,
    'PowerQuadratic': eq.power_quadratic,
    'Logarithmic': eq.logarithmic,
    'MichaelisMenten': eq.michaelis_menten,
    'Lomolino': eq.lomolino
}

def calculate_richness(areas, params):
    results = []
    for area in areas:
        richness = []
        for model_name, param_set in params.items():
            if model_name in models:
                model_func = models[model_name]
                # Extract parameters and handle None for b2
                b0, b1, b2 = param_set
                params_list = [area, float(b0), float(b1)]
                if b2 is not None:
                    params_list.append(float(b2))
                richness.append(model_func(*params_list))
        mean_richness = np.mean(richness)
        results.append([area, mean_richness])
    return results

def estimate_species_richness(areas, custom_params):
    return calculate_richness(areas, custom_params)


####################################################################################
# Not relevant to run the script

def main():
    # Check if script is executed directly
    if len(sys.argv) > 1:
        # If command-line arguments are provided, treat each as an area
        areas = [float(arg) for arg in sys.argv[1:]]
        params = {
            'Power': [20.81, 0.1896, None],  # Example parameters, adjust as needed
            'PowerQuadratic': [1.35, 0.1524, 0.0081],
            'Logarithmic': [14.36, 21.16, None],
            'MichaelisMenten': [85.91, 42.57, None],
            'Lomolino': [1082.45, 1.59, 390000000]
        }
        results = calculate_richness(areas, params)
        for result in results:
            print(f"Area: {result[0]}, Estimated Richness: {result[1]}")
    else:
        # Homework answers or other default functionality can be added here
        # For now, it will just print the message as specified
        print("This is just a bunch of equations for use by other programs. It doesn't do anything on its own. TTFN.")

if __name__ == "__main__":
    main()

# Function to be called when imported