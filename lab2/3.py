def make_dict(n):
    d = {}
    for i in range(1, n+1):
        d[i] = i*i
    return d

if __name__ == '__main__':
    n = int(input("n: "))
    d = make_dict(n)
    for i in d.keys():
        print(str(i)+":", d[i])