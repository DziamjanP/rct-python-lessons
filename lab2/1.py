def main(n):
    s = 0
    for i in range(n):
        if (i+1) % 2 == 0:
            s += i+1
    print(s)

if __name__ == '__main__':
    n = int(input("n: "))
    main(n)
    print(2 * sum(range(0, n // 2 + 1)))