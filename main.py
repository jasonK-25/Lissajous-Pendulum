import matplotlib.pyplot as plt
from mass_loss import mass_loss
from basic import basic
import numpy as np

g = 9.81
mu = 0.001
mb = 1
ms0 = 2
rho = 1600
aeff = 10
a = 0.07
b = 0.2


lx = 16
ly = 25

x0 = 0
y0 = 1

vx0 = 1.6
vy0 = 0

#beta = 0.01
beta = 0.01
q = 0.01

start_t = 0
end_t = 60
num_data_pt = 1000

alpha = 1/(rho * np.pi * a**2)

basic.plot_basic_drag(lx, ly, x0, y0, vx0, vy0, ms0 + mb, beta, g, start_t, end_t, num_data_pt)
#mass_loss.plot_linear(lx, ly, x0, y0, vx0, vy0, mb, ms0, q, beta, b, alpha, g, start_t, end_t, num_data_pt)
#mass_loss.plot_exp(lx, ly, x0, y0, vx0, vy0, mb, ms0, q, beta, b, alpha, g, start_t, end_t, num_data_pt)
mass_loss.plot_fluid(lx, ly, x0, y0, vx0, vy0, mb, ms0, q, beta, mu, rho, a, b, aeff, alpha, g, start_t, end_t, num_data_pt)

plt.title(f"lx={lx}, ly={ly}, x0={x0}, y0={y0}, vx0={vx0}, vy0={vy0}, \na={a}, b={b}, rho={rho}, q={q}, beta={beta}, t=[{start_t}, {end_t}]")
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.show()