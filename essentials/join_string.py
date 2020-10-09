def split_and_join(line):
    return "-".join(line.split(" "))


def mutate_string(string, position, character):
    data = list(string)
    print(data, position)
    data[position] = character
    return "".join(data)


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
