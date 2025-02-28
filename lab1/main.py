import math

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
    x, y = map(float, input("x, y: ").split())
    print(g(x, y))  