from original import plot_original, plot_original_resistance
from mass_loss import plot_simple_linear, plot_resistance_linear, plot_simple_exponential, plot_simple_fluid, plot_resistance_fluid
import matplotlib.pyplot as plt
import math

fig, graph = plt.subplots()

mu = 0.001
mb = 1
ms0 = 2
rho = 1600
aeff = 9.81
a = 0.07
b = 1
q = 0.001
lx = 4
ly = 9
Ax = 1/4
Ay = 1/9
psix = 0
psiy = 0

beta = 0.01

end_t = 60
num_data_pt = 1000

plot_original(lx, ly, Ax, Ay, psix, psiy, end_t, num_data_pt)
plot_original_resistance(lx, ly, Ax, Ay, psix, psiy, ms0+mb, beta, end_t, num_data_pt)
#plot_simple_linear(mb, ms0, rho, a, b, q, lx, ly, Ax, Ay, psix, psiy, end_t, num_data_pt)
#plot_resistance_linear(mb, ms0, rho, beta, a, b, q, lx, ly, Ax, Ay, psix, psiy, end_t, num_data_pt)
#plot_simple_exponential(mb, ms0, rho, a, b, q, lx, ly, Ax, Ay, psix, psiy, end_t, num_data_pt)
#
# plot_simple_fluid(mb, ms0, mu, rho, aeff, a, b, lx, ly, Ax, Ay, psix, psiy, end_t, num_data_pt)
#plot_resistance_fluid(mb, ms0, mu, rho, beta, aeff, a, b, lx, ly, Ax, Ay, psix, psiy, end_t, num_data_pt)
plt.legend(loc="best")
plt.xlabel("x")
plt.ylabel("y")
plt.show()