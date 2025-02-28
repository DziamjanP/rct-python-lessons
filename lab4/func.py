import matplotlib.pyplot as plt
import numpy as np
import math
#this isn't finished

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


if __name__ == '__main__':
    xs = np.linspace(0, 2, 100)
    y = []
    for x in xs:
        y.append(b(x, 2))
    plt.scatter(xs, y)
    plt.title("Funcitons")

    plt.savefig("plots/func.png", bbox_inches='tight')
    plt.savefig("plots/func.pdf", bbox_inches='tight')
