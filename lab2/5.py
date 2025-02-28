def find_nums(array):
    new_array = []
    for num in array: 
        if num % 3 == 0: new_array.append(num)
    return new_array

if __name__ == '__main__':
    array = map(int, input("array: ").split())
    array = map(str, find_nums(array))
    print(", ".join(array))