def find_longest_str(l):
    maxstr = l[0]
    for i in l:
        if len(i) > len(maxstr): maxstr = i
    return maxstr

if __name__ == '__main__':
    l = [
        'abcdefg',
        '123456',
        '0',
        'asgfagra',
        '',
        '0123456789',
        'aer4a',
        'adaaaaaaa'
    ]
    print(find_longest_str(l))