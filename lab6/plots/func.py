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

def get_plot():
    xs = np.linspace(0, 2, 100000)
    y1 = []
    y2 = []
    for x in xs:
        y1.append(b(x, 2))
        y2.append(g(x, 2))

    fig, ax1 = plt.subplots(dpi=400)

    ax1.set_xlabel("x")
    ax1.scatter(xs, y1, s=1, label="g(x, b=2)")
    ax1.set_ylabel("g(x, b=2)", color="C0")
    
    ax2 = ax1.twinx()
    ax2.set_ylabel("b(x, y=2)", color="red")

    ax2.scatter(xs, y2, color="red", s=1, label="b(x, y=2)")

    fig.legend()

    return fig
