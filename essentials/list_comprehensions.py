def print_combinations(i, j, k, n):
    result = []
    for a in range(0, i+1):
        for b in range(0, j+1):
            for c in range(0, k+1):
                if(a+b+c != n):
                    result.append([a, b, c])
    print(result)


if __name__ == '__main__':
    i = int(input("Enter i :"))
    j = int(input("Enter j :"))
    k = int(input("Enter k :"))
    n = int(input("Enter n :"))
    print_combinations(i, j, k, n)
