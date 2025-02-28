import matplotlib.pyplot as plt
import numpy as np
#this isn't finished

def f(x):
    return x*x

def g(x, y):
    
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
    plt.scatter(x, y)
    plt.title("Funciton")

    plt.savefig("plots/func.png", bbox_inches='tight')
    plt.savefig("plots/func.pdf", bbox_inches='tight')
