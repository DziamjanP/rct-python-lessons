import matplotlib.pyplot as plt
import numpy as np
import math
#vars 11 & 14

def f(x):
    return x*x

def b(x, y):
    
    if y == 0:
        b = 0
    elif x == 0:
        b = (f(x) ** 2 + y) ** 3
    elif x / y < 0:
        b = math.log(abs(f(x)/y)) + (f(x) + y) ** 3 
    else:
        b = math.log(f(x)) + (f(x) ** 2 + y) ** 3 
    return b

def g(x, b):
    xb = x*b
    if 0.5 < xb < 10:
        return math.exp(f(x) - abs(b))
    elif 0.1 < xb < 0.5:
        return abs(f(x) + b) ** 0.5
    else:
        return 2 * f(x) * f(x)

def get_plot(start_x, end_x, var_b = 2, var_y = 2):
    xs = np.linspace(start_x, end_x, 100000)
    y1 = []
    y2 = []
    for x in xs:
        y1.append(b(x, var_y))
        y2.append(g(x, var_b))

    fig, ax1 = plt.subplots(dpi=400)

    ax1.set_xlabel("x")
    ax1.scatter(xs, y1, s=1, label=f"g(x, b={var_b})")
    ax1.set_ylabel(f"g(x, b={var_b})", color="C0")
    
    ax2 = ax1.twinx()
    ax2.set_ylabel(f"b(x, y={var_y})", color="red")

    ax2.scatter(xs, y2, color="red", s=1, label=f"b(x, y={var_y})")

    fig.legend()

    return fig
