def paliandrome(number):
    num = number
    rev = 0
    while(num != 0):
        rem = num % 10
        num = int(num/10)
        rev = rev*10 + rem    # Here we calculate reverse
    return number == rev


if __name__ == "__main__":
    number = int(input("Enter the Number:"))
    res = f'{number} is paliandrom'if paliandrome(
        number) else f'{number} is not paliandrom'
    print(res)
