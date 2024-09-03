def check(num):
    return num%11 == 0

num = int(input("Enter your number: "))
print("number is divisible by 11", check(num))