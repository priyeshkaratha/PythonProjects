def minion_game(string):
    vowels = list('AEIOU')

    kw = []
    st = []

    for i in string:
        if i in vowels:
            kw.append(i)
        else:
            st.append(i)
    kw = list(set(kw))
    st = list(set(st))
    print(kw, st)

    for i in range(len(string)+1):
        for j in kw:
            print(string[0:i], string.count(string[0:i], 0, len(string)))


if __name__ == '__main__':
    s = input("Enter number:")
    minion_game(s)
