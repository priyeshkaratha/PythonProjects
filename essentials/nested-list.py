def print_second(array):
    array2 = []
    for i in array:
        array2.append(i[1])
    data = find_runnerupp(array2)
    numbers = []
    for i in array:
        if(i[1] == data):
            numbers.append(i[0])
    numbers.sort()
    for i in numbers:
        print(i)


def find_runnerupp(arr):
    arr = list(dict.fromkeys(arr))
    i = min(arr)
    arr.remove(i)
    return min(arr)


if __name__ == '__main__':
    array = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        array.append([name, score])
    print_second(array)
