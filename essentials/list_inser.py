array = []
def execute(command):
    c = command.split(" ")
    if(c[0] == "append"):
        array.append(int(c[1]))
    elif(c[0] == "insert"):
        array.insert(int(c[1]), int(c[2]))
    elif(c[0] == "sort"):
        array.sort()
    elif(c[0] == "remove"):
        array.remove(int(c[1]))
    elif(c[0] == "pop"):
        array.pop()
    elif(c[0] == "reverse"):
        array.reverse()
    elif(c[0] == "print"):
        print(array)

if __name__ == '__main__':
    N = int(input())
    for i in range(0,N):
        command = input()
        execute(command)