import matplotlib.pyplot as plt
from mass_loss import mass_loss
from basic import basic
import numpy as np

mu = 0.001
mb = 1
ms0 = 2
rho = 1600
aeff = 10
a = 0.07
b = 0.2
q = 0.01
lx = 4
ly = 9
Ax = 1/4
Ay = 1/9
psix = 0
psiy = 0

beta = 0.01

start_t = 0
end_t = 10
num_data_pt = 1000

alpha = 1/(rho * np.pi * a**2)

basic.plot_basic_drag(lx, ly, Ax, Ay, psix, psiy, ms0 + mb, beta, end_t, num_data_pt)
mass_loss.plot_linear(lx, ly, Ax, Ay, psix, psiy, mb, ms0, q, beta, b, alpha, start_t, end_t, num_data_pt)
mass_loss.plot_exp(lx, ly, Ax, Ay, psix, psiy, mb, ms0, q, beta, b, alpha, start_t, end_t, num_data_pt)
mass_loss.plot_fluid(lx, ly, Ax, Ay, psix, psiy, mb, ms0, q, beta, mu, rho, a, b, aeff, alpha, start_t, end_t, num_data_pt)

plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.show()