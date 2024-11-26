"""
This module contains various mathematical equations for use in species-area relationship calculations and population growth models.

Functions:
- power: Calculates species richness using a power function.
- power_quadratic: Calculates species richness using a quadratic power function.
- logarithmic: Calculates species richness using a logarithmic function.
- michaelis_menten: Calculates species richness using the Michaelis-Menten equation.
- lomolino: Calculates species richness using the Lomolino model.
"""

import numpy as np

def power(area, b0, b1, b2=None):
    """Calculates species richness using a power function."""
    return float(b0) * (area ** float(b1))

def power_quadratic(area, b0, b1, b2):
    """Calculates species richness using a quadratic power function."""
    return 10 ** (float(b0) + float(b1) * np.log10(area) + float(b2) * (np.log10(area) ** 2))

def logarithmic(area, b0, b1, b2=None):
    """Calculates species richness using a logarithmic function."""
    return float(b0) + float(b1) * np.log(area)

def michaelis_menten(area, b0, b1, b2=None):
    """Calculates species richness using the Michaelis-Menten equation."""
    return float(b0) * area / (float(b1) + area)

def lomolino(area, b0, b1, b2):
    """Calculates species richness using the Lomolino model."""
    return float(b0) / (1 + (float(b1) ** ((np.log(area)) ** (float(b2) / area))))

# Optional direct execution check
if __name__ == "__main__":
    print("This is just a bunch of equations for use by other programs. It doesn't do anything on its own. TTFN.")
