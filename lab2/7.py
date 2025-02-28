def check_palindrome(s: int):
    i = 0
    while (len(s) - 2 * i > 1):
        if (s[i] != s[len(s)-i-1]): break
        i += 1
    return len(s) - 2 * i <= 1

if __name__ == '__main__':
    s = input("str: ").strip()
    print(s, "is" if check_palindrome(s) else "is not", "a palindrome")