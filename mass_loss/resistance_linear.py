import matplotlib.pyplot as plt
import numpy as np
import math


def get_ms(t, ms0, q):
    return ms0 - (q*t)

def get_M(ms, mb):
    return mb + ms

def get_h(ms, mb, b, alpha):
    return ((mb *  b) + (alpha * ms**2))/(2*(mb + ms))

def get_wx(lx, b, h, g=9.81):
    return (g/(lx + b - h))**(1/2)

def get_wy(ly, b, h, g=9.81):
    return (g/(ly + b - h))**(1/2)

def get_x(t, Ax, wx, beta, ms, psix, g=9.81):
    return Ax * math.exp(-beta/(2*ms) * t) * math.cos(wx * t + psix)

def get_y(t, Ay, wy, beta, ms, psiy, g=9.81):
    return Ay * math.exp(-beta/(2*ms) * t) * math.cos(wy * t + psiy)

get_ms = np.vectorize(get_ms)
get_M = np.vectorize(get_M)
get_h = np.vectorize(get_h)
get_wx = np.vectorize(get_wx)
get_wy = np.vectorize(get_wy)
get_x = np.vectorize(get_x)
get_y = np.vectorize(get_y)

def plot_resistance_linear(mb, ms0, rho, beta, a, b, q, lx, ly, Ax, Ay, psix, psiy, end_t, num_data_pt):

    
    max_t = round(ms0 / q)
    if end_t > max_t:
        print("Linear Mass Loss -- time reached allowed maximum, time capped at maximum")
        end_t = max_t
    alpha = 1/(rho * math.pi * a**2)

    start_t = 0

    t_array = np.linspace(start_t, end_t, num_data_pt)

    ms_array = get_ms(t_array, ms0, q)
    M_array = get_M(ms_array, mb)
    h_array = get_h(ms_array, mb, b, alpha)
    wx_array = get_wx(lx, b, h_array)
    wy_array = get_wy(ly, b, h_array)
    x_array = get_x(t_array, Ax, wx_array, beta, ms_array, psix)
    y_array = get_y(t_array, Ay, wy_array, beta, ms_array, psiy)

    plt.plot(x_array, y_array, label="linear")
    plt.scatter(x_array[0], y_array[0])