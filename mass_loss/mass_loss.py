import matplotlib.pyplot as plt
import numpy as np


def get_linear_ms(t, ms0, q):
    if t > ms0/q:
        return 0
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

def get_w_underdamp(M, l, b, h, beta, g):
    #return 1/(2*M) * ((4 * M**2 * g)/(l) - beta**2)**(1/2)
    return 1/(2*M) * ((4 * M**2 * g)/(l + b - h) - beta**2)**(1/2)

def get_w1_overdamp(M, l, b, h, beta, g):
    return (- beta - (beta**2 - ((4 * M**2 * g)/(l + b - h)))**(1/2)) / (2*M)

def get_w2_overdamp(M, l, b, h, beta, g):
    return (- beta + (beta**2 - ((4 * M**2 * g)/(l + b - h)))**(1/2)) / (2*M)

def get_ordinate_underdamp(t, A, B, beta, M, w):
    return np.exp(-beta/(2*M) * t) * ((A * np.cos(w * t)) + (B * np.sin(w * t)))

def get_ordinate_crit_damp(t, A, B, beta, M, w):
    return (A + (B*t)) * np.exp(-beta/(2*M) * t)

def get_ordinate_overdamp(t, A, B, w1, w2):
    return (A * np.exp(w1 * t)) + (B * np.exp(w2 * t))


get_linear_ms = np.vectorize(get_linear_ms)
get_exp_ms = np.vectorize(get_exp_ms)
get_fluid_ms = np.vectorize(get_fluid_ms)
get_M = np.vectorize(get_M)
get_h = np.vectorize(get_h)
get_w_underdamp = np.vectorize(get_w_underdamp)
get_w1_overdamp = np.vectorize(get_w1_overdamp)
get_w2_overdamp = np.vectorize(get_w2_overdamp)

get_ordinate_underdamp = np.vectorize(get_ordinate_underdamp)
get_ordinate_crit_damp = np.vectorize(get_ordinate_crit_damp)
get_ordinate_overdamp = np.vectorize(get_ordinate_overdamp)

def __plot_mass_loss_underdamp(lx:float, ly:float, x0:float, y0:float, vx0:float, vy0:float, mb:float, ms0:float, q:float, beta:float, b:float, alpha:float, t_array, ms_array, plot_label:str, g):

    M_array = get_M(ms_array, mb)
    h_array = get_h(ms_array, mb, b, alpha)
    wx_array = get_w_underdamp(M_array, lx, b, h_array, beta, g)
    wy_array = get_w_underdamp(M_array, ly, b, h_array, beta, g)

    Ax = x0
    Bx = (vx0 + ((Ax * beta)/(2 * M_array[0]))) / (wx_array[0]) 
    Ay = y0
    By = (vy0 + ((Ay * beta)/(2 * M_array[0]))) / (wy_array[0])


    x_array = get_ordinate_underdamp(t_array, Ax, Bx, beta, M_array, wx_array)
    y_array = get_ordinate_underdamp(t_array, Ay, By, beta, M_array, wy_array)

    plt.plot(x_array, y_array, label=plot_label)
    plt.scatter(x_array[0], y_array[0])

def __plot_mass_loss_crit_damp(lx:float, ly:float, x0:float, y0:float, vx0:float, vy0:float, mb:float, ms0:float, q:float, beta:float, b:float, alpha:float, t_array, ms_array, plot_label:str, g):

    M_array = get_M(ms_array, mb)
    h_array = get_h(ms_array, mb, b, alpha)
    
    Ax = x0
    Bx = vx0 + ((Ax * beta)/(2 * M_array))
    Ay = y0
    By = vy0 + ((Ay * beta)/(2 * M_array))

    x_array = get_ordinate_crit_damp(t_array, Ax, Bx, beta, M_array)
    y_array = get_ordinate_crit_damp(t_array, Ay, By, beta, M_array)

    plt.plot(x_array, y_array, label=plot_label)
    plt.scatter(x_array[0], y_array[0])

def __plot_mass_loss_overdamp(lx:float, ly:float, x0:float, y0:float, vx0:float, vy0:float, mb:float, ms0:float, q:float, beta:float, b:float, alpha:float, t_array, ms_array, plot_label:str, g):

    M_array = get_M(ms_array, mb)
    h_array = get_h(ms_array, mb, b, alpha)

    w1x_array = get_w1_overdamp(h_array, lx, b, h_array, beta, g)
    w2x_array = get_w1_overdamp(h_array, lx, b, h_array, beta, g)
    w1y_array = get_w1_overdamp(h_array, ly, b, h_array, beta, g)
    w2y_array = get_w2_overdamp(h_array, ly, b, h_array, beta, g)

    Bx = (vx0 - (x0 * w1x[0]))/(w2x[0] - w1x[0])
    Ax = x0 - Bx
    By = (vy0 - (y0 * w1y[0]))/(w2y[0] - w1y[0])
    Ay = y0 - By

    x_array = get_ordinate_overdamp(t_array, Ax, Bx, w1x_array, w2x_array)
    y_array = get_ordinate_overdamp(t_array, Ay, By, w1y_array, w2y_array)

    plt.plot(x_array, y_array, label=plot_label)
    plt.scatter(x_array[0], y_array[0])

def plot_linear(lx:float, ly:float, x0:float, y0:float, vx0:float, vy0:float, mb:float, ms0:float, q:float, beta:float, b:float, alpha:float, g, start_t:int, end_t:int, num_data_pt:int):
    t_array = np.linspace(start_t, end_t, num_data_pt)
    ms_array = get_linear_ms(t_array, ms0, q)
    __plot_mass_loss_underdamp(lx, ly, x0, y0, vx0, vy0, mb, ms0, q, beta, b, alpha, t_array, ms_array, f"linear", g)

def plot_exp(lx:float, ly:float, x0:float, y0:float, vx0:float, vy0:float, mb:float, ms0:float, q:float, beta:float, b:float, alpha:float, g, start_t:int, end_t:int, num_data_pt:int):
    t_array = np.linspace(start_t, end_t, num_data_pt)
    ms_array = get_exp_ms(t_array, ms0, q)
    __plot_mass_loss_underdamp(lx, ly, x0, y0, vx0, vy0, mb, ms0, q, beta, b, alpha, t_array, ms_array, "exp", g)


def plot_fluid(lx:float, ly:float, x0:float, y0:float, vx0:float, vy0:float, mb:float, ms0:float, q:float, beta:float, mu:float, rho:float, a:float, b:float, aeff:float, alpha:float, g, start_t:int, end_t:int, num_data_pt:int):
    max_t = (2 * (ms0)**(1/2))/(mu * a * (2 * rho * np.pi * aeff)**(1/2))
    t_array = np.linspace(start_t, end_t, num_data_pt)
    ms_array = get_fluid_ms(t_array, ms0, mu, a, rho, aeff, max_t)
    __plot_mass_loss_underdamp(lx, ly, x0, y0, vx0, vy0, mb, ms0, q, beta, b, alpha, t_array, ms_array, "fluid", g)


