import numpy as np
import matplotlib.pyplot as plt

body_mass = [32000, 37800, 347000, 4200, 196500, 100000, 4290, 32000,
65000, 69125, 9600, 133300, 150000, 407000, 115000, 67000, 325000,
21500, 58588, 65320, 85000, 135000, 20500, 1613, 1618]

metabolic_rate = [49.984, 51.981, 306.770, 10.075, 230.073, 148.949,
11.966, 46.414, 123.287, 106.663, 20.619, 180.150, 200.830,
224.779, 148.940, 112.430, 286.847, 46.347, 142.863, 106.670,
119.660, 104.150, 33.165, 4.900, 4.865]

log_body_mass = np.log(body_mass)

log_metabolic_rate = np.log(metabolic_rate)

plt.plot(body_mass, metabolic_rate, "o-g")
plt.title("Body_mass_vs | metabolic_rate_vs")
plt.xlabel("Body")
plt.ylabel("Metabolic")
plt.grid(True)
plt.legend(["Body_mass","Metabolic"])
plt.show()

plt.plot(log_body_mass, log_metabolic_rate, "o-g")
plt.title("Log_Body_mass_vs | log_metabolic_rate_vs")
plt.xlabel("log_Body")
plt.ylabel("log_Metabolic")
plt.grid(True)
plt.legend(["log_Body_mass","log_Metabolic"])
plt.show()

plt.plot(body_mass, "o-g")
plt.show()

plt.plot(metabolic_rate, "o-g")
plt.show()

plt.plot(log_body_mass, "o-g")
plt.show()

plt.plot(log_metabolic_rate, "o-g")
plt.show()

plt.plot(body_mass, "o-g")
plt.plot(metabolic_rate, "v--m")
plt.show()