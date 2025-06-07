import matplotlib.pyplot as plt
import numpy as np


def get_x(t, Ax, lx, psix, g=9.81):
    return Ax * np.cos((g/lx)**(1/2) * t + psix)

def get_y(t, Ay, ly, psiy, g=9.81):
    return Ay * np.cos((g/ly)**(1/2) * t + psiy)

get_x = np.vectorize(get_x)
get_y = np.vectorize(get_y)

def plot_original(lx, ly, Ax, Ay, psix, psiy, end_t, num_data_pt):

    start_t = 0

    t_array = np.linspace(start_t, end_t, num_data_pt)
    x_array = get_x(t_array, Ax, lx, psix)
    y_array = get_y(t_array, Ay, ly, psiy)

    plt.plot(x_array, y_array, label="original")
    plt.scatter(x_array[0], y_array[0])