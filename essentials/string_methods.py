if __name__ == '__main__':
    s = input()
    res = {
        "isalnum": False,
        "isalpha": False,
        "isdigit": False,
        "islower": False,
        "isupper": False
    }

    for i in list(s):
        if(res["isalnum"] == False):
            res["isalnum"] = i.isalnum()
        if(res["isalpha"] == False):
            res["isalpha"] = i.isalpha()
        if(res["isdigit"] == False):
            res["isdigit"] = i.isdigit()
        if(res["islower"] == False):
            res["islower"] = i.islower()
        if(res["isupper"] == False):
            res["isupper"] = i.isupper()

    print(res["isalnum"])
    print(res["isalpha"])
    print(res["isdigit"])
    print(res["islower"])
    print(res["isupper"])
