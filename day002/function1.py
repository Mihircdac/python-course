num1=int(input("enter 1st number "))
num2=int(input("enter 2nd number "))


def calc(num1,num2):
    num3 = num1 + num2
    num1*=num1
    raised=num1**num2
    print(num3,"is the added number")
    print(num1,"is the square")
    print(raised,"is the power raised number of 1st to 2nd")
    
calc(num1,num2)

