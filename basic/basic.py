import matplotlib.pyplot as plt
import numpy as np


def get_w_underdamp(M, l, beta, g, discriminant):
    return (-discriminant)**(1/2) / (2 * M)

def get_w1_overdamp(M, l, beta, g, discriminant):
    return (- beta + discriminant**(1/2))/ (2*M)

def get_w2_overdamp(M, l, beta, g, discriminant):
    return (- beta - discriminant**(1/2))/ (2*M)

def get_ordinate_underdamp(t, A, B, w, beta, M):
    return np.exp(-beta/(2*M) * t) * ((A * np.cos(w * t)) + (B * np.sin(w * t)))

def get_ordinate_crit_damp(t, A, B, beta, M):
    return (A + Bt) * np.exp(-beta/(2*M) * t)

def get_ordinate_overdamp(t, A, B, w1, w2):
    return (A * np.exp(w1 * t)) + (B * np.exp(w2 * t))

get_ordinate_underdamp = np.vectorize(get_ordinate_underdamp)
get_ordinate_crit_damp = np.vectorize(get_ordinate_crit_damp)
get_ordinate_overdamp = np.vectorize(get_ordinate_overdamp)

def plot_basic_drag(lx:float, ly:float, x0:float, y0:float, vx0:float, vy0:float, M:float, beta:float, g:float, start_t:int, end_t:int, num_data_pt:int):
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

    t_array = np.linspace(start_t, end_t, num_data_pt)

    discriminant_x = beta**2 - ((4 * M**2 * g)/lx)
    discriminant_y = beta**2 - ((4 * M**2 * g)/ly)
    if discriminant_x < 0:
        print("x underdamp")
        wx = get_w_underdamp(M, lx, beta, g, discriminant_x)
        Ax = x0
        Bx = (vx0 + ((beta * x0)/(2 * M))) / wx
        x_array = get_ordinate_underdamp(t_array, Ax, Bx, wx, beta, M)
    
    elif discriminant_x == 0:
        print("x critical damp")
        Ax = x0
        Bx = vx0 + ((Ax * beta)/(2 * M))
        x_array = get_ordinate_crit_damp(t_array, Ax, Bx, beta, M)
    
    elif discriminant_x > 0:
        print("x overdamp")
        w1x = get_w1_overdamp(M, lx, beta, g, discriminant_x)
        w2x = get_w2_overdamp(M, lx, beta, g, discriminant_x)
        Bx = (vx0 - (x0 * w1x))/(w2x - w1x)
        Ax = x0 - Bx
        x_array = get_ordinate_overdamp(t_array, Ax, Bx, w1x, w2x)
        

    if discriminant_y < 0:
        print("y underdamp")
        wy = get_w_underdamp(M, ly, beta, g, discriminant_y)
        Ay = y0
        By = (vy0 + ((beta * y0)/(2 * M))) / wy
        y_array = get_ordinate_underdamp(t_array, Ay, By, wy, beta, M)

    elif discriminant_y == 0:
        print("y overdamp")
        Ay = y0
        By = vy0 + ((Ay * beta)/(2 * M))
        y_array = get_ordinate_crit_damp(t_array, Ay, By, beta, M)

    elif discriminant_y > 0:
        print("y overdamp")
        w1y = get_w1_overdamp(M, ly, beta, g, discriminant_y)
        w2y = get_w2_overdamp(M, ly, beta, g, discriminant_y)
        By = (vy0 - (y0 * w1y))/(w2y - w1y)
        Ay = y0 - By
        y_array = get_ordinate_overdamp(t_array, Ay, By, w1y, w2y)
       
    plt.plot(x_array, y_array, label="basic drag")
    plt.scatter(x_array[0], y_array[0])