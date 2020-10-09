if __name__ == '__main__':
    n = int(input())
    i = 0
    integer_list = tuple(map(int, input().split()))
    print(integer_list)
    print(hash(integer_list))    