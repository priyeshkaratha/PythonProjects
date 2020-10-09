def find_runnerupp(arr):
    print(arr)
    return max(arr.remove(max(list(dict.fromkeys(arr)))))


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split(" ")))
    print(find_runnerupp(arr))
