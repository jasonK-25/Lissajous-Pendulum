import matplotlib.pyplot as plt
import numpy as np


def get_w(M, l, beta, g=9.81):
    #temp = 4 * M**2 * g
    #if beta > temp:
    #    beta = temp
    #    print("Original Resistance -- beta reached allowed maximum, beta capped at maximum")
    return 1/(2*M) * ((4 * M**2 * g)/l - beta)**(1/2)

def get_ordinate(t, A, w, beta, M, psi):
    return A * np.exp(-beta/(2*M) * t) * np.cos(w * t + psi)

get_ordinate = np.vectorize(get_ordinate)

def plot_basic_drag(lx:float, ly:float, Ax:float, Ay:float, psix:float, psiy:float, M:float, beta:float, end_t:int, num_data_pt:int):
    """plot simple 2D pendulum with drag modelled linearly to velocity

    Args:
        lx (float): length of string in x direction
        ly (float): length of string in y direction
        Ax (float): Amplitude in x direction
        Ay (float): Amplitude in y direction
        psix (float): phase offset in x direction
        psiy (float): phase offset in y direction
        M (float): total mass
        beta (float): coefficient of drag
        end_t (int): ending time for model
        num_data_pt (int): number of data points to be plotted
    """

    start_t = 0

    t_array = np.linspace(start_t, end_t, num_data_pt)
    wx = get_w(M, lx, beta)
    wy = get_w(M, ly, beta)
    x_array = get_ordinate(t_array, Ax, wx, beta, M, psix)
    y_array = get_ordinate(t_array, Ay, wy, beta, M, psiy)

    plt.plot(x_array, y_array, label="basic drag")
    plt.scatter(x_array[0], y_array[0])