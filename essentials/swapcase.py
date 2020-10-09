def swap_case(s):
    strd = ""
    for i in s:
        strd += i.swapcase()
    return strd


if __name__ == '__main__':
    data = input()
    print(swap_case(data))
