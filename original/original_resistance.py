import matplotlib.pyplot as plt
import numpy as np
import math


def get_wx(t, M, lx, beta, g=9.81):#
    temp = 4 * M**2 * g
    if beta > temp:
        beta = temp
        print("Original Resistance -- beta reached allowed maximum, beta capped at maximum")
    return 1/(2*M) * (temp/lx - beta)**(1/2)

def get_wy(t, M, ly, beta, g=9.81):
    temp = 4 * M**2 * g
    if beta > temp:
        beta = temp
        print("Original Resistance -- beta reached allowed maximum, beta capped at maximum")
    return 1/(2*M) * (temp/ly - beta)**(1/2)

def get_x(t, Ax, wx, beta, M, psix):
    return Ax * math.exp(-beta/(2*M) * t) * math.cos(wx * t + psix)

def get_y(t, Ay, wy, beta, M, psiy):
    return Ay * math.exp(-beta/(2*M) * t) * math.cos(wy * t + psiy)

get_wx = np.vectorize(get_wx)
get_wy = np.vectorize(get_wy)
get_x = np.vectorize(get_x)
get_y = np.vectorize(get_y)

def plot_original_resistance(lx, ly, Ax, Ay, psix, psiy, M, beta, end_t, num_data_pt):

    start_t = 0

    t_array = np.linspace(start_t, end_t, num_data_pt)
    wx_array = get_wx(t_array, M, lx, beta)
    wy_array = get_wx(t_array, M, ly, beta)
    x_array = get_x(t_array, Ax, wx_array, beta, M, psix)
    y_array = get_y(t_array, Ay, wy_array, beta, M, psiy)

    plt.plot(x_array, y_array, label="original resistance")
    plt.scatter(x_array[0], y_array[0])