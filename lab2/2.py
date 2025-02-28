def proc(l):
    s = set()
    nl = []
    for i in l:
        if not i in s:
            nl.append(i)
        s.add(i)
    return nl

if __name__ == '__main__':
    l = map(int, input("array: ").split())
    l = map(str, proc(l))
    print(", ".join(l))