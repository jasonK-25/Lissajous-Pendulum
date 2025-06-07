import matplotlib.pyplot as plt
import numpy as np


def get_linear_ms(t, ms0, q):
    return ms0 - (q*t)

def get_exp_ms(t, ms0, q):
    return ms0*np.exp(-q*t)

def get_fluid_ms(t, ms0, mu, a, rho, aeff, max_t):    

    if t >= max_t: 
        print("bottle is empty")
        return 0
    return 0.25 * ((2*(ms0**(1/2))) - (mu * a * (2 * rho * np.pi * aeff)**(1/2) * t))**2

def get_M(ms, mb):
    return mb + ms

def get_h(ms, mb, b, alpha):
    return ((mb * b) + (alpha * (ms**2)))/(2*(mb + ms))

def get_w(M, l, b, h, beta, g=9.81):

    return 1/(2*M) * ((4 * M**2 * g)/(l + b) - beta)**(1/2)
    return 1/(2*M) * ((4 * M**2 * g)/(l + b - h) - beta)**(1/2)

def get_ordinate(t, A, w, beta, M, psi):
    return A * np.exp(-beta/(2*M) * t) * np.cos(w * t + psi)


get_linear_ms = np.vectorize(get_linear_ms)
get_exp_ms = np.vectorize(get_exp_ms)
get_fluid_ms = np.vectorize(get_fluid_ms)
get_M = np.vectorize(get_M)
get_h = np.vectorize(get_h)
get_w = np.vectorize(get_w)
get_ordinate = np.vectorize(get_ordinate)

def __plot_mass_loss(lx:float, ly:float, Ax:float, Ay:float, psix:float, psiy:float, mb:float, ms0:float, q:float, beta:float, b:float, alpha:float, t_array, ms_array, plot_label:str, g=9.81):

    M_array = get_M(ms_array, mb)
    h_array = get_h(ms_array, mb, b, alpha)
    wx_array = get_w(M_array, lx, b, h_array, beta, g)
    wy_array = get_w(M_array, ly, b, h_array, beta, g)
    x_array = get_ordinate(t_array, Ax, wx_array, beta, M_array, psix)
    y_array = get_ordinate(t_array, Ay, wy_array, beta, M_array, psiy)

    plt.plot(x_array, y_array, label=plot_label)
    plt.scatter(x_array[0], y_array[0])

def plot_linear(lx:float, ly:float, Ax:float, Ay:float, psix:float, psiy:float, mb:float, ms0:float, q:float, beta:float, b:float, alpha:float, start_t:int, end_t:int, num_data_pt:int, g=9.81):
    t_array = np.linspace(start_t, end_t, num_data_pt)
    ms_array = get_linear_ms(t_array, ms0, q)
    __plot_mass_loss(lx, ly, Ax, Ay, psix, psiy, mb, ms0, q, beta, b, alpha, t_array, ms_array, "linear", g)

def plot_exp(lx:float, ly:float, Ax:float, Ay:float, psix:float, psiy:float, mb:float, ms0:float, q:float, beta:float, b:float, alpha:float, start_t:int, end_t:int, num_data_pt:int, g=9.81):
    t_array = np.linspace(start_t, end_t, num_data_pt)
    ms_array = get_exp_ms(t_array, ms0, q)
    __plot_mass_loss(lx, ly, Ax, Ay, psix, psiy, mb, ms0, q, beta, b, alpha, t_array, ms_array, "exp", g)


def plot_fluid(lx:float, ly:float, Ax:float, Ay:float, psix:float, psiy:float, mb:float, ms0:float, q:float, beta:float, mu:float, rho:float, a:float, b:float, aeff:float, alpha:float, start_t:int, end_t:int, num_data_pt:int, g=9.81):
    max_t = (2 * (ms0)**(1/2))/(mu * a * (2 * rho * np.pi * aeff)**(1/2))
    t_array = np.linspace(start_t, end_t, num_data_pt)
    ms_array = get_fluid_ms(t_array, ms0, mu, a, rho, aeff, max_t)
    __plot_mass_loss(lx, ly, Ax, Ay, psix, psiy, mb, ms0, q, beta, b, alpha, t_array, ms_array, "fluid", g)

