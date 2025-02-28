def check_palindrome(n: int):
    l = []
    while n != 0:
        l.append(n % 10)
        n = n // 10
    i = 0
    while i < round(len(l) / 2):
        if (l[i] != l[len(l)-i-1]): break
        i += 1
    
    return i == round(len(l) / 2)

if __name__ == '__main__':
    n = int(input("n: "))
    print(n, "is" if check_palindrome(n) else "is not", "a palindrome")