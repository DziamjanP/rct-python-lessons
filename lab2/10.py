def fib_n(n):
    fibs = [1, 1]
    next_n = 2
    while (next_n <= n):
        fibs.append(next_n)
        next_n = fibs[len(fibs) - 1] + fibs[len(fibs) - 2]
    return fibs

if __name__ == '__main__':
    n = int(input("n: "))
    print(", ".join(map(str, fib_n(n))))