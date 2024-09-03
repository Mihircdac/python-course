num1=int(input("enter 1st number "))
num2=int(input("enter 2nd number "))


def calc(num1,num2):
    num3 = num1 + num2
    print(num3,"is the added number")
    num1*=num1
    print(num1,"is the square")
    raised=num1**num2
    print(raised,"is the power raised number of 1st to 2nd")
    
calc(num1,num2)

